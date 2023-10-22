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

#returns a list of cells to add to the KB as false
def axiom_1_false_cells(symbol):
    list_of_false_cells = []
    symbol_parts = str(symbol).split('_')

    row = symbol_parts[0]
    column = symbol_parts[1]

    if row in friends:
        for friend in friends:
            if friend != row and not pl_resolution(new_kb, expr('~'+ year + '_' + column)):
                list_of_false_cells.append(friend + '_' + column)
    if row in activities:
       for activity in activities:
            if activity != row and not pl_resolution(new_kb, expr('~'+ year + '_' + column)):
                list_of_false_cells.append(activity + '_' + column)
    if row in years:
        for year in years:
            if year != row and not pl_resolution(new_kb, expr('~'+ year + '_' + column)):
                list_of_false_cells.append(year + '_' + column)
    if column in friends:
        for friend in friends:
            if friend != column and not pl_resolution(new_kb, expr('~'+ year + '_' + column)):
                list_of_false_cells.append(row + '_' + friend)
    if column in activities:
        for activity in activities:
            if activity != column and not pl_resolution(new_kb, expr('~'+ year + '_' + column)):
                list_of_false_cells.append(row + '_' + activity)
    if column in years:
        for year in years:
            if year != column and not pl_resolution(new_kb, expr('~'+ year + '_' + column)):
                list_of_false_cells.append(row + '_' + year)
    return list_of_false_cells

    
#AXIOM #6
friends = ['G', 'L', 'P', 'V']
activities = ['C', 'HG', 'KY', 'SD']
years = ['y1', 'y2', 'y3', 'y4']

combined_year_and_friend = [year + '_' + friend for year in years for friend in friends]
combined_year_and_activity = [year + '_' + activity for year in years for activity in activities]
combined_friend_and_activity = [activity + '_' + friend for activity in activities for friend in friends]

total_symbols = combined_year_and_friend + combined_year_and_activity + combined_friend_and_activity

total_symbols_prop = [expr(symbol) for symbol in total_symbols]

y1_G, y1_L, y1_P, y1_V, y2_G, y2_L, y2_P, y2_V, y3_G, y3_L, y3_P, y3_V, y4_G, y4_L, y4_P, y4_V, y1_C, y1_HG, y1_KY, y1_SD, y2_C, y2_HG, y2_KY, y2_SD, y3_C, y3_HG, y3_KY, y3_SD, y4_C, y4_HG, y4_KY, y4_SD, C_G, C_L, C_P, C_V, HG_G, HG_L, HG_P, HG_V, KY_G, KY_L, KY_P, KY_V, SD_G, SD_L, SD_P, SD_V = expr("y1_G, y1_L, y1_P, y1_V, y2_G, y2_L, y2_P, y2_V, y3_G, y3_L, y3_P, y3_V, y4_G, y4_L, y4_P, y4_V, y1_C, y1_HG, y1_KY, y1_SD, y2_C, y2_HG, y2_KY, y2_SD, y3_C, y3_HG, y3_KY, y3_SD, y4_C, y4_HG, y4_KY, y4_SD, C_G, C_L, C_P, C_V, HG_G, HG_L, HG_P, HG_V, KY_G, KY_L, KY_P, KY_V, SD_G, SD_L, SD_P, SD_V")

#print(total_symbols_prop)
#print(len(total_symbols))

new_kb = PropKB()


#active clue 1:
new_kb.tell((y1_SD |'<=>'| y3_HG))
new_kb.tell(y2_SD |'<=>'| y4_HG)

#active clue 2:
new_kb.tell(KY_G ^ y4_G)
new_kb.tell(~y4_KY)

#active clue 3:
new_kb.tell(y3_L)

#active clue 4:
new_kb.tell(~(y3_HG))
new_kb.tell(~(y3_V))
new_kb.tell(~(y3_G))
new_kb.tell(~(HG_V))
new_kb.tell(~(HG_G))

#ADD MORE TO KB BASED UPON AXIOMS

#AXIOM #1 - IF A CELL IS TRUE, ALL THE CELLS IN IT'S ROW AND COLUMN ARE FALSE

def is_in_kb(kb, symbol):
    for clause in kb.clauses:
        if expr(symbol) == expr(clause):
            return True
    return False

while True:

    for symbol in total_symbols_prop:
        if pl_resolution(new_kb, symbol):
            #print("found: ", symbol)
            #print("fill the rest of the cells as false")
            list_of_false_cells = axiom_1_false_cells(symbol)
            #print("list of false cells: ", list_of_false_cells)
            for false_cell in list_of_false_cells:
                new_kb.tell(~expr(false_cell))
            
    print(new_kb.clauses)

    #AXIOM #2 - IF THERE ARE 3 CELLS IN A COLUMN OR ROW THAT ARE FALSE, THE FINAL UNKNOWN CELL MUST BE TRUE

    # years, activities

    for year in years:
        for activity in activities:
            #print("looking at: ", year + '_' + activity)
            false_count = 0
            #if a true cell is found there is no need to analyze the row or column
            if pl_resolution(new_kb, expr(year + '_' + activity)):
                break
            elif pl_resolution(new_kb, expr('~'+ year + '_' + activity)):
                #print("false cell found")
                #print("found: ", expr('~'+ year + '_' + activity))
                false_count += 1
            else:
                #print("empty cell found")
                empty_cell = expr(year + '_' + activity)
        if false_count == 3:
            print("AXIOM 2 Satisfied, filling final cell as true")
            new_kb.tell(empty_cell)
                
                
    # years, friends

    for year in years:
        for friend in friends:
            #print("looking at: ", year + '_' + friend)
            false_count = 0
            #if a true cell is found there is no need to analyze the row or column
            if pl_resolution(new_kb, expr(year + '_' + friend)):
                break
            elif pl_resolution(new_kb, expr('~'+ year + '_' + friend)):
                #print("false cell found")
                #print("found: ", expr('~'+ year + '_' + friend))
                false_count += 1
            else:
                #print("empty cell found")
                empty_cell = expr(year + '_' + friend)



    # activities, friends

    for activity in activities:
        for friend in friends:
            #print("looking at: ", activity + '_' + friend)
            false_count = 0
            #if a true cell is found there is no need to analyze the row or column
            if pl_resolution(new_kb, expr(activity + '_' + friend)):
                break
            elif pl_resolution(new_kb, expr('~'+ activity + '_' + friend)):
                #print("false cell found")
                #print("found: ", expr('~'+ activity + '_' + friend))
                false_count += 1
            else:
                #print("empty cell found")
                empty_cell = expr(activity + '_' + friend)
        if false_count == 3:
            print("AXIOM 2 Satisfied, filling final cell as true")
            new_kb.tell(empty_cell)


    #AXIOM #3 - IF TWO VALUES IN TWO DIFFERENT SUBGRIDS ARE TRUE AND THEY SHARE AN ELEMENT, THEN THE VALUE THAT COMBINES BOTH OF THE VALUES MUST BE TRUE.
    #           IF THOSE TWO VALUES ARE NOT BOTH TRUE, THEN THE THIRD VALUE MUST BE FALSE.


    # grid 0 & 1 predict grid 2

    # IF (person & year) & (activity & year), THEN (person and activity)
    # IF ~[(person & year) & (activity & year)], THEN ~(person and activity)

    def axiom_3(outside_loop, middle_loop, inside_loop):
        iterations = 0
        for value_1 in outside_loop:
            for value_2 in middle_loop:
                for value_3 in inside_loop:
                    print("Looking at: "+value_2 + '_' + value_3)
                    iterations += 1
                    if pl_resolution(new_kb, expr(value_1 + '_' + value_2)) and pl_resolution(new_kb, expr(value_1 + '_' + value_3)) and not pl_resolution(new_kb, expr(value_2 + '_' + value_3)):
                        new_kb.tell(expr(value_2 + '_' + value_3))
                        print("FOUND 1: ", expr(value_2 + '_' + value_3))
                    elif pl_resolution(new_kb, expr('~'+ value_1 + '_' + value_2)) and pl_resolution(new_kb, expr(value_1 + '_' + value_3)) and not pl_resolution(new_kb, expr('~'+ value_2 + '_' + value_3)):
                        new_kb.tell(expr('~'+ value_2 + '_' + value_3))
                        print("FOUND 3: ", expr('~'+ value_2 + '_' + value_3))
                    elif pl_resolution(new_kb, expr(value_1 + '_' + value_2)) and pl_resolution(new_kb, expr('~'+ value_1 + '_' + value_3)) and not pl_resolution(new_kb, expr('~'+ value_2 + '_' + value_3)):
                        new_kb.tell(expr('~'+ value_2 + '_' + value_3))
                        print("FOUND 4: ", expr('~'+ value_2 + '_' + value_3))
                    else:
                        print("nothing")
        return iterations
    
    '''
    for year in years:
        for friend in friends:
            for activity in activity:
                if pl_resolution(new_kb, expr(year + '_' + friend)) and pl_resolution(new_kb, expr(year + '_' + activity)):
                    new_kb.tell(expr(friend + '_' + activity))
                if(pl_resolution(new_kb, expr('~'+ year + '_' + friend)) and pl_resolution(new_kb, expr('~'+ year + '_' + activity))):
                    new_kb.tell(expr('~'+ friend + '_' + activity))
                if(pl_resolution(new_kb, expr('~'+ year + '_' + friend)) and pl_resolution(new_kb, expr(year + '_' + activity))):
                    new_kb.tell(expr('~'+ friend + '_' + activity))
                if(pl_resolution(new_kb, expr(year + '_' + friend)) and pl_resolution(new_kb, expr('~'+ year + '_' + activity))):
                    new_kb.tell(expr('~'+ friend + '_' + activity))
    '''



    print(axiom_3(years, activities, friends))
    print("\n\n")
    #grid 0 and 2 predict grid 1

    # IF (year and person) & (activity and person), THEN (year and activity)
    # IF ~[(year and person) & (activity and person)], THEN ~(year and activity)

    '''
    for year in years:
        for friend in friends:
            for activity in activity:
                if pl_resolution(new_kb, expr(year + '_' + friend)) and pl_resolution(new_kb, expr(year + '_' + activity)):
                    new_kb.tell(expr(friend + '_' + activity))
                if(pl_resolution(new_kb, expr('~'+ year + '_' + friend)) and pl_resolution(new_kb, expr('~'+ year + '_' + activity))):
                    new_kb.tell(expr('~'+ friend + '_' + activity))
                if(pl_resolution(new_kb, expr('~'+ year + '_' + friend)) and pl_resolution(new_kb, expr(year + '_' + activity))):
                    new_kb.tell(expr('~'+ friend + '_' + activity))
                if(pl_resolution(new_kb, expr(year + '_' + friend)) and pl_resolution(new_kb, expr('~'+ year + '_' + activity))):
                    new_kb.tell(expr('~'+ friend + '_' + activity))
    '''

    print(axiom_3(friends, years, activities))
    print("\n\n")

    #grid 1 and 2 predict grid 0


    # IF (year and activity) & (person and activity), THEN (year and person)

    print(axiom_3(activities, years, friends))
    print("\n\n")


