from other import *
from utils import Expr, expr, first
import itertools
from main import PropKB
#active clue # 1 :
    # (SD & y1) <==> (HG & y3)
    # (SD & y2) <==> (HG & y4)

# active clue # 2 :
    # (G & KY) ^ (G & y4)

# active clue # 3 :
    # (L & y3)

# active clue # 4 :
# ~(y3 & HG)
# ~(y3 & V)
# ~(y3 & G)
# ~(HG & V)
# ~(HG & G)

#AXIOM #1 - IF A CELL IS TRUE, ALL THE CELLS IN IT'S ROW AND COLUMN ARE FALSE
# if pl_resolution(our_kb, (C & 2)):
    #print("fill the rest of the cells as false")
    # our_kb.tell(!(A & 2) & !(B & 2) & !(D & 2) & !(C & 1) & !(C & 3) & !(C & 4))

#AXIOM #2 - IF THERE ARE 3 CELLS IN A COLUMN OR ROW THAT ARE FALSE, THE FINAL UNKNOWN CELL MUST BE TRUE

# AXIOM #3 - IF (activity1 & person1) ^ (year1 & person1), THEN !(year1 and activity1)
# Ex: IF gladys is either camping but not in 2004, or gladys is going on vacation in 2004 but not camping, THEN that means that camping cannot occur in 2004

# grid 0 & 1 predict grid 2

# AXIOM #4 - IF (activity1 & year1) & (person1 & year1), THEN (person1 and activity1)
# EX: IF hangliding happens in 2004 and pam's activity is in 2004, THEN pam must be hang gliding

# AXIOM #5 - IF ![(activity1 & year1) & (person1 & year1)], THEN !(person1 and activity1)

#grid 0 and 1 predict grid 2

# grid 0 and 2 predict grid 1

  #AXIOM #6 - IF (person1 & year1) & (activity1 & year1), THEN (person1 and activity1)
  
  #AXIOM #7 - IF ![(person1 & year1) & (activity1 & year1)], THEN !(person1 and activity1)

# grid 1 and 0 predict grid 2

#grid 1 and 2 predict grid 0

#grid 2 and 0 predict grid 1

#grid 2 and 1 predict grid 0



#AXIOM #6
friends = ['G', 'L', 'P', 'V']
activities = ['C', 'HG', 'KY', 'SD']
years = ['y1', 'y2', 'y3', 'y4']


#GLADYS, LILLIE, PAM, VICTOR
G, L, P, V = expr('G, L, P, V ')

#activites
#CAMPING, HANG GLIDING, KAYAKYING, SKYDIVING
C, HG, KY, SD = expr('C, HG, KY, SD')

#years
y1, y2, y3, y4 = expr('y1, y2, y3, y4')

combined_year_and_friend = [year + '-' + friend for year in years for friend in friends]
combined_year_and_activity = [year + '-' + activity for year in years for activity in activities]
combined_friend_and_activity = [friend + '-' + activity for friend in friends for activity in activities]

total_symbols = combined_year_and_friend + combined_year_and_activity + combined_friend_and_activity

print(total_symbols)
print(len(total_symbols))

sg_0 = list(itertools.product(years,friends))

sg_1 = list(itertools.product(years,activities))

sg_2 = list(itertools.product(friends,activities))



new_kb = PropKB()

# (SD & y1) <==> (HG & y3)
# (SD & y2) <==> (HG & y4)

#LOADING INITIAL KNOWLEDGE BASE WITH ACTIVE CLUES

#active clue 1:
#new_kb.tell((SD & y1) |'<=>'| (HG & y3))

#active clue 2:
#new_kb.tell((G & KY) ^ (G & y4))

#active clue 3:
new_kb.tell(L & y3)
new_kb.tell(L & C)
new_kb.tell(G & y1)

#print(pl_resolution(new_kb, (L & G)))
#active clue 4:
#new_kb.tell(~(y3 & HG))
#new_kb.tell(~(y3 & V))
#new_kb.tell(~(y3 & G))
#new_kb.tell(~(HG & V))
#new_kb.tell(~(HG & G))

print(new_kb.clauses)

#print(pl_resolution())

#print(sg_0_combos)
#print(sg_1_combos)
#print(sg_2_combos)


#if pl_resolution(our_kb, (KY | y4)):

