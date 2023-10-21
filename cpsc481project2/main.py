from other import *
from utils import Expr, expr, first
import itertools

class KB:
    """
    A knowledge base to which you can tell and ask sentences.
    To create a KB, subclass this class and implement tell, ask_generator, and retract.
    Ask_generator：
      For a Propositional Logic KB, ask(P & Q) returns True or False, but for an
      FOL KB, something like ask(Brother(x, y)) might return many substitutions
      such as {x: Cain, y: Abel}, {x: Abel, y: Cain}, {x: George, y: Jeb}, etc.
      So ask_generator generates these one at a time, and ask either returns the
      first one or returns False.
    """

    def __init__(self, sentence=None):
        raise NotImplementedError

    def tell(self, sentence):
        """Add the sentence to the KB."""
        raise NotImplementedError

    def ask(self, query):
        """Return a substitution that makes the query true, or, failing that, return False."""
        return first(self.ask_generator(query), default=False)

    def ask_generator(self, query):
        """Yield all the substitutions that make query true."""
        raise NotImplementedError

    def retract(self, sentence):
        """Remove sentence from the KB."""
        raise NotImplementedError


class PropKB(KB):
    """A KB for propositional logic. Inefficient, with no indexing."""

    def __init__(self, sentence=None):
        self.clauses = []
        if sentence:
            self.tell(sentence)

    def tell(self, sentence):
        """Add the sentence's clauses to the KB."""
        self.clauses.extend(conjuncts(to_cnf(sentence)))

    def ask_generator(self, query):
        """Yield the empty substitution {} if KB entails query; else no results."""
        if tt_entails(Expr('&', *self.clauses), query):
            yield {}

    def ask_if_true(self, query):
        """Return True if the KB entails query, else return False."""
        for _ in self.ask_generator(query):
            return True
        return False

    def retract(self, sentence):
        """Remove the sentence's clauses from the KB."""
        for c in conjuncts(to_cnf(sentence)):
            if c in self.clauses:
                self.clauses.remove(c)


def KB_AgentProgram(KB):
    """A generic logical knowledge-based agent program. [Figure 7.1]"""
    steps = itertools.count()

    def program(percept):
        t = next(steps)
        KB.tell(make_percept_sentence(percept, t))
        action = KB.ask(make_action_query(t))
        KB.tell(make_action_sentence(action, t))
        return action

    def make_percept_sentence(percept, t):
        return Expr("Percept")(percept, t)

    def make_action_query(t):
        return expr("ShouldDo(action, {})".format(t))

    def make_action_sentence(action, t):
        return Expr("Did")(action[expr('action')], t)

    return program





#clauses = []
# SG# = Subgrid Number(#) 
# ex: Subgrid 1 = SG0

#Clue3part1 = expr('L & 2003')

our_kb = PropKB()

#friends 
#GLADYS, LILLIE, PAM, VICTOR
G, L, P, V = expr('G, L, P, V ')

#activites
#CAMPING, HANG GLIDING, KAYAKYING, SKYDIVING
C, HG, KY, SD = expr('C, HG, KY, SD')

#years
y1, y2, y3, y4 = expr('y1, y2, y3, y4')

#Cells

#negation      =   ~
#and           =   &
#or            =   |
#Xor           =   ^
#implication   =   ==>
#Reverse       =   <==
#equivalance   =   <=>

#add propositional logic statements
#our_kb.tell(y3 & L)
# our_kb.tell(G & (KY | y4))
#our_kb.tell()
#our_kb.tell((V & y1) | (V & y2))
#our_kb.tell(G | '<=>' | L)

our_kb.tell((G) & (KY | y4))
our_kb.tell((~(HG | C)))
#call print our clauses
print(our_kb.clauses)





#pl_resolution takes in (knowledgebase, propositional statement)
#if false 
print(pl_resolution(our_kb, (KY | y4)))







"""
G = Gladys
L = Lille
P = Pam
V = Victor

C = camping
H = hang gliding
K = kayaking
S = Skydiving

11, 12, 13, 14, 15, 16, 17, 18
21, 22, 23, 24, 25, 26, 27, 28
31, 32, 33, 34, 35, 36, 37, 38
41, 42, 43, 44, 45, 46, 47, 48
51, 52, 53, 54
61, 62, 63, 64
71, 72, 73, 74
81, 82, 83, 84

was thinking of separating every 4 cells horizontal
by putting them in a list

like list:
2001    = [11, 12, 13, 14]
2001b   = [15, 16, 17, 18]
2002    = [21, 22, 23, 24]
2022b   = [25, 26, 27, 28]
2003    = [31, 32, 33, 34]
2003b   = [35, 36, 37, 38]
2004    = [41, 42, 43, 44]
2004b   = [45, 46, 47, 48]
camp    = [51, 52, 53, 54]
hglide  = [61, 62, 63, 64]
kayak   = [71, 72, 73, 74]
skydiv  = [81, 82, 83, 84]

we can then designate columns by getting the third value
in the expression 

example = list = ['p11, 'p12']
print(list[1][0]) = p
print(list[1][1]) = 1
print(list[1][2]) = 2

we can then (if we want) append all the columns into a new
list like

if list[1][1] = 1:
    gladys.append(list[1])
    #append cell 11 to gladys or something like that


I think however the cells might be separted like 

(as in row 2001 with first letter and x,y values)
#G11 = Gladys x:1, y:1
G11, L12, P13, V14

we can define symbols like how the logic.ipynb file did

G11, L12, P13, V14 = expr('G11, L12, P13, V14')

we also need a Clauses list that has the 4 basic clues
in propisitional statements

clause = []

we can input new inferences and clues by creating an object

our_kb = Propkb()

and then call it with the tell function

our_kb.tell("insert statement")
EX:

"lille went on a vacation in 2003
our_kb.tell(~L12)
our_kb.tell(~L22)
our_kb.tell(~L42)
"telling our knowledge base that its not 2001, 2002, 2004"

this should be appending to our clauses
we can check by doing
our_kb.clauses



"""
