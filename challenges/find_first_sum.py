"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def index_of(i, element, list): 
    try: 
        return list.index(element, i + 1)
    except ValueError: 
        return -1 

def find_first_sum(nums, goal):
    for i, num in enumerate(nums): 
        num_look_for = goal - num
        index_wanted = index_of(i, num_look_for, nums)
        if index_wanted != -1: 
            return [i, index_wanted] 
    return None   



nums = [4, 4, 5, 6, 2]
goal = 8
   
print(find_first_sum(nums, goal))