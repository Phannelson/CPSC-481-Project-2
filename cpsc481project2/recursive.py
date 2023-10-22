people = ['G', 'L', 'P', 'V']
activity = ['C', 'HG', 'KY', 'SD']
year = ['y1', 'y2', 'y3', 'y4']
variables_list = [['y1_G', 'y1_L', 'y1_P', 'y1_V', 
    'y2_G', 'y2_L', 'y2_P', 'y2_V', 
    'y3_G', 'y3_L', 'y3_P', 'y3_V', 
    'y4_G', 'y4_L', 'y4_P', 'y4_V'], 
    ['y1_C', 'y1_HG', 'y1_KY', 'y1_SD', 
    'y2_C', 'y2_HG', 'y2_KY', 'y2_SD', 
    'y3_C', 'y3_HG', 'y3_KY', 'y3_SD', 
    'y4_C', 'y4_HG', 'y4_KY', 'y4_SD'],
    ['C_G', 'C_L', 'C_P', 'C_V', 
    'HG_G', 'HG_L', 'HG_P', 'HG_V', 
    'KY_G', 'KY_L', 'KY_P', 'KY_V', 
    'SD_G', 'SD_L', 'SD_P', 'SD_V']]

def zeroout(old_combination, original):
    combination = old_combination.copy()
    first, second = original.split('_')
    if isYear(first):
        if isPerson(second):
            for person in people:
                var = first + '_' + person
                if shoudlZeroOut(original,var,combination):
                    combination[first + '_' + person] = False
                
            for y in year:
                var = y + '_' + second
                if shoudlZeroOut(original,var,combination):
                    combination[y + '_' + second] = False

        elif isActivity(second):
            for a in activity:
                var = first + '_' + a
                if shoudlZeroOut(original,var,combination):
                    combination[first + '_' + a] = False
            
            for y in year:
                var = y + '_' + second
                if shoudlZeroOut(original,var,combination):
                    combination[y + '_' + second] = False
             
    if isActivity(first):
        if isPerson(second):
            for person in people:
                var = first + '_' + person
                if shoudlZeroOut(original,var,combination):
                    combination[first + '_' + person] = False
            for a in activity:
                var = a + '_' + second
                if shoudlZeroOut(original,var,combination):
                    combination[a + '_' + second] = False
                    
    if combination[original] == False:
        combination[original] = True
        
    return combination
            
def isYear(variable):
    return variable in year

def isPerson(variable):
    return variable in people

def isActivity(variable):
    return variable in activity

def shoudlZeroOut(original,var,combination):
    return (var != original and var not in combination)

listOfCombinations = []
    

def generate_combinations(variables, current=None, index=0):
    """
    Recursively generate combinations of True/False for the given list of variables.
    
    Parameters:
    - variables: List of variable names.
    - current_combination: Current combination being built.
    - index: Index of the current variable being processed.
    
    Returns:
    - A list of dictionaries, each representing a combination.
    """
    if current is None:
        current_combination = {}
    else:
        current_combination = current.copy()
        


    # Base case: if all variables have been processed, return the current combination
    if index == len(variables):
        if (current_combination not in listOfCombinations) and sumTrue(current_combination) == 4:
            listOfCombinations.append(current_combination.copy())
        return
    
    # Recursive case: set the current variable to True and recurse, then set to False and recurse
    variable = variables[index]
    if variable not in current_combination:
        current_combination[variable] = True
        zeroed_out = zeroout(current_combination, variable)
        generate_combinations(variables, zeroed_out, index + 1)
        
        current_combination[variable] = False
        if (index+1 < len(variables)):
            generate_combinations(variables, current_combination, index + 1)
    else: 
        generate_combinations(variables, current_combination, index + 1)

    return 

def sumTrue(combination):
    sum = 0
    for x in combination:
        if combination[x] == True:
            sum += 1
    return sum


def make_sentense(grid):
    # Todo Make sensentes to check with the axiosm
    
    
    
# Get the first 5 combinations for demonstration purposes
for grid in variables_list:
    generate_combinations(grid)
    for gridState in listOfCombinations:
        make_sentense(gridState)
        
print(len(listOfCombinations))
print(listOfCombinations)