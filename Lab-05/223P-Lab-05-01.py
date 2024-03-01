# Write a Python function called process_data that takes three parameters -

# a name (string)
# age (integer)
# and height (float) -
# and returns a tuple containing these values. Additionally, write another function  display_info that takes a tuple as a parameter and unpacks it to print the information in the 
# following format: "Name: [name], Age: [age], Height: [height]".

def process_data(name, age, height):
    return (name, age, height)

def display_info(info):
    name, age, height = info
    print(f"Name: {name}, Age: {age}, Height: {height}")
    
    
data_tuple = process_data("Ryan", 1, 1.2)
display_info(data_tuple)
    