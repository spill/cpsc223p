# Write a Python function  set_operations that takes two sets as parameters and performs the following set of operations:

# Calculate and print the union of the two sets.
# Calculate and print the intersection of the two sets.
# Calculate and print the set difference (elements in the first set but not in the second).
# Additionally, write another function called display_set that takes a set as a parameter and prints its elements.


def set_operations(set1, set2):
    print("set1 U set2", set1.union(set2))
    
    print("set1 intersection set2", set1.intersection(set2))
    
    print("Set difference in setA but not setB", set1.difference(set2))
    
def display_set(set):
    set1, set2= set
    print("Elements of the sets:", set)
    
    
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}

set_operations(set1, set2)


    
    
