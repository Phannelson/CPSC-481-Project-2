import itertools

variables_list = [
    'y1_G', 'y1_L', 'y1_P', 'y1_V', 
    'y2_G', 'y2_L', 'y2_P', 'y2_V', 
    'y3_G', 'y3_L', 'y3_P', 'y3_V', 
    'y4_G', 'y4_L', 'y4_P', 'y4_V', 
    'y1_C', 'y1_HG', 'y1_KY', 'y1_SD', 
    'y2_C', 'y2_HG', 'y2_KY', 'y2_SD', 
    'y3_C', 'y3_HG', 'y3_KY', 'y3_SD', 
    'y4_C', 'y4_HG', 'y4_KY', 'y4_SD', 
    'C_G', 'C_L', 'C_P', 'C_V', 
    'HG_G', 'HG_L', 'HG_P', 'HG_V', 
    'KY_G', 'KY_L', 'KY_P', 'KY_V', 
    'SD_G', 'SD_L', 'SD_P', 'SD_V']

# Using iterators to generate combinations
combinations_iterator = itertools.product([True, False], repeat=len(variables_list))

# Displaying the first 5 combinations for demonstration
first_5_combinations = []

for idx, combination in enumerate(combinations_iterator):
    if idx == 5:  # Only taking the first 5 combinations
        break
    combination_dict = {variables_list[i]: value for i, value in enumerate(combination)}
    first_5_combinations.append(combination_dict)

print("First 5 combinations: ")
print(first_5_combinations)