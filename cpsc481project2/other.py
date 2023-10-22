from cpsc481project2.utils import *

def is_symbol(s):
    """A string s is a symbol if it starts with an alphabetic char.
    >>> is_symbol('R2D2')
    True
    """
    return isinstance(s, str) and s[:1].isalpha()


def is_var_symbol(s):
    """A logic variable symbol is an initial-lowercase string.
    >>> is_var_symbol('EXE')
    False
    """
    return is_symbol(s) and s[0].islower()


def is_prop_symbol(s):
    """A proposition logic symbol is an initial-uppercase string.
    >>> is_prop_symbol('exe')
    False
    """
    return is_symbol(s) and s[0].isupper()


def variables(s):
    """Return a set of the variables in expression s.
    >>> variables(expr('F(x, x) & G(x, y) & H(y, z) & R(A, z, 2)')) == {x, y, z}
    True
    """
    return {x for x in subexpressions(s) if is_variable(x)}


def is_definite_clause(s):
    """
    Returns True for exprs s of the form A & B & ... & C ==> D,
    where all literals are positive.  In clause form, this is
    ~A | ~B | ... | ~C | D, where exactly one clause is positive.
    >>> is_definite_clause(expr('Farmer(Mac)'))
    True
    """
    if is_symbol(s.op):
        return True
    elif s.op == '==>':
        antecedent, consequent = s.args
        return (is_symbol(consequent.op) and
                all(is_symbol(arg.op) for arg in conjuncts(antecedent)))
    else:
        return False


def parse_definite_clause(s):
    """Return the antecedents and the consequent of a definite clause."""
    assert is_definite_clause(s)
    if is_symbol(s.op):
        return [], s
    else:
        antecedent, consequent = s.args
        return conjuncts(antecedent), consequent


# Useful constant Exprs used in examples and code:
A, B, C, D, E, F, G, P, Q, x, y, z = map(Expr, 'ABCDEFGPQxyz')

def to_cnf(s):
    """Convert a propositional logical sentence to conjunctive normal form.
    That is, to the form ((A | ~B | ...) & (B | C | ...) & ...) [p. 253]
    >>> to_cnf('~(B | C)')
    (~B & ~C)
    """
    s = expr(s)
    if isinstance(s, str):
        s = expr(s)
    s = eliminate_implications(s)  # Steps 1, 2 from p. 253
    s = move_not_inwards(s)  # Step 3
    return distribute_and_over_or(s)  # Step 4


def eliminate_implications(s):
    """Change implications into equivalent form with only &, |, and ~ as logical operators."""
    s = expr(s)
    if not s.args or is_symbol(s.op):
        return s  # Atoms are unchanged.
    args = list(map(eliminate_implications, s.args))
    a, b = args[0], args[-1]
    if s.op == '==>':
        return b | ~a
    elif s.op == '<==':
        return a | ~b
    elif s.op == '<=>':
        return (a | ~b) & (b | ~a)
    elif s.op == '^':
        assert len(args) == 2  # TODO: relax this restriction
        return (a & ~b) | (~a & b)
    else:
        assert s.op in ('&', '|', '~')
        return Expr(s.op, *args)


def move_not_inwards(s):
    """Rewrite sentence s by moving negation sign inward.
    >>> move_not_inwards(~(A | B))
    (~A & ~B)
    """
    s = expr(s)
    if s.op == '~':
        def NOT(b):
            return move_not_inwards(~b)

        a = s.args[0]
        if a.op == '~':
            return move_not_inwards(a.args[0])  # ~~A ==> A
        if a.op == '&':
            return associate('|', list(map(NOT, a.args)))
        if a.op == '|':
            return associate('&', list(map(NOT, a.args)))
        return s
    elif is_symbol(s.op) or not s.args:
        return s
    else:
        return Expr(s.op, *list(map(move_not_inwards, s.args)))


def distribute_and_over_or(s):
    """Given a sentence s consisting of conjunctions and disjunctions
    of literals, return an equivalent sentence in CNF.
    >>> distribute_and_over_or((A & B) | C)
    ((A | C) & (B | C))
    """
    s = expr(s)
    if s.op == '|':
        s = associate('|', s.args)
        if s.op != '|':
            return distribute_and_over_or(s)
        if len(s.args) == 0:
            return False
        if len(s.args) == 1:
            return distribute_and_over_or(s.args[0])
        conj = first(arg for arg in s.args if arg.op == '&')
        if not conj:
            return s
        others = [a for a in s.args if a is not conj]
        rest = associate('|', others)
        return associate('&', [distribute_and_over_or(c | rest)
                               for c in conj.args])
    elif s.op == '&':
        return associate('&', list(map(distribute_and_over_or, s.args)))
    else:
        return s


def associate(op, args):
    """Given an associative op, return an expression with the same
    meaning as Expr(op, *args), but flattened -- that is, with nested
    instances of the same op promoted to the top level.
    >>> associate('&', [(A&B),(B|C),(B&C)])
    (A & B & (B | C) & B & C)
    >>> associate('|', [A|(B|(C|(A&B)))])
    (A | B | C | (A & B))
    """
    args = dissociate(op, args)
    if len(args) == 0:
        return _op_identity[op]
    elif len(args) == 1:
        return args[0]
    else:
        return Expr(op, *args)


_op_identity = {'&': True, '|': False, '+': 0, '*': 1}


def dissociate(op, args):
    """Given an associative op, return a flattened list result such
    that Expr(op, *result) means the same as Expr(op, *args).
    >>> dissociate('&', [A & B])
    [A, B]
    """
    result = []

    def collect(subargs):
        for arg in subargs:
            if arg.op == op:
                collect(arg.args)
            else:
                result.append(arg)

    collect(args)
    return result


def conjuncts(s):
    """Return a list of the conjuncts in the sentence s.
    >>> conjuncts(A & B)
    [A, B]
    >>> conjuncts(A | B)
    [(A | B)]
    """
    return dissociate('&', [s])


def disjuncts(s):
    """Return a list of the disjuncts in the sentence s.
    >>> disjuncts(A | B)
    [A, B]
    >>> disjuncts(A & B)
    [(A & B)]
    """
    return dissociate('|', [s])


def tt_entails(kb, alpha):
  """
  [Figure 7.10]
  Does kb entail the sentence alpha? Use truth tables. For propositional
  kb's and sentences. Note that the 'kb' should be an Expr which is a
  conjunction of clauses.
  >>> tt_entails(expr('P & Q'), expr('Q'))
  True
  """
  assert not variables(alpha)
  symbols = list(prop_symbols(kb & alpha))
  return tt_check_all(kb, alpha, symbols, {})


def tt_check_all(kb, alpha, symbols, model):
  """Auxiliary routine to implement tt_entails."""
  if not symbols:
      if pl_true(kb, model):
          result = pl_true(alpha, model)
          assert result in (True, False)
          return result
      else:
          return True
  else:
      P, rest = symbols[0], symbols[1:]
      return (tt_check_all(kb, alpha, rest, extend(model, P, True)) and
              tt_check_all(kb, alpha, rest, extend(model, P, False)))


def prop_symbols(x):
  """Return the set of all propositional symbols in x."""
  if not isinstance(x, Expr):
      return set()
  elif is_prop_symbol(x.op):
      return {x}
  else:
      return {symbol for arg in x.args for symbol in prop_symbols(arg)}


def constant_symbols(x):
  """Return the set of all constant symbols in x."""
  if not isinstance(x, Expr):
      return set()
  elif is_prop_symbol(x.op) and not x.args:
      return {x}
  else:
      return {symbol for arg in x.args for symbol in constant_symbols(arg)}


def predicate_symbols(x):
  """Return a set of (symbol_name, arity) in x.
  All symbols (even functional) with arity > 0 are considered."""
  if not isinstance(x, Expr) or not x.args:
      return set()
  pred_set = {(x.op, len(x.args))} if is_prop_symbol(x.op) else set()
  pred_set.update({symbol for arg in x.args for symbol in predicate_symbols(arg)})
  return pred_set


def tt_true(s):
  """Is a propositional sentence a tautology?
  >>> tt_true('P | ~P')
  True
  """
  s = expr(s)
  return tt_entails(True, s)


def pl_true(exp, model={}):
  """Return True if the propositional logic expression is true in the model,
  and False if it is false. If the model does not specify the value for
  every proposition, this may return None to indicate 'not obvious';
  this may happen even when the expression is tautological.
  >>> pl_true(P, {}) is None
  True
  """
  if exp in (True, False):
      return exp
  op, args = exp.op, exp.args
  if is_prop_symbol(op):
      return model.get(exp)
  elif op == '~':
      p = pl_true(args[0], model)
      if p is None:
          return None
      else:
          return not p
  elif op == '|':
      result = False
      for arg in args:
          p = pl_true(arg, model)
          if p is True:
              return True
          if p is None:
              result = None
      return result
  elif op == '&':
      result = True
      for arg in args:
          p = pl_true(arg, model)
          if p is False:
              return False
          if p is None:
              result = None
      return result
  p, q = args
  if op == '==>':
      return pl_true(~p | q, model)
  elif op == '<==':
      return pl_true(p | ~q, model)
  pt = pl_true(p, model)
  if pt is None:
      return None
  qt = pl_true(q, model)
  if qt is None:
      return None
  if op == '<=>':
      return pt == qt
  elif op == '^':  # xor or 'not equivalent'
      return pt != qt
  else:
      raise ValueError('Illegal operator in logic expression' + str(exp))


def pl_resolution(kb, alpha):
  """
  [Figure 7.12]
  Propositional-logic resolution: say if alpha follows from KB.
  >>> pl_resolution(horn_clauses_KB, A)
  True
  """
  clauses = kb.clauses + conjuncts(to_cnf(~alpha))
  new = set()
  while True:
      n = len(clauses)
      pairs = [(clauses[i], clauses[j])
               for i in range(n) for j in range(i + 1, n)]
      for (ci, cj) in pairs:
          resolvents = pl_resolve(ci, cj)
          if False in resolvents:
              return True
          new = new.union(set(resolvents))
      if new.issubset(set(clauses)):
          return False
      for c in new:
          if c not in clauses:
              clauses.append(c)


def pl_resolve(ci, cj):
  """Return all clauses that can be obtained by resolving clauses ci and cj."""
  clauses = []
  for di in disjuncts(ci):
      for dj in disjuncts(cj):
          if di == ~dj or ~di == dj:
              clauses.append(associate('|', unique(remove_all(di, disjuncts(ci)) + remove_all(dj, disjuncts(cj)))))
  return clauses
