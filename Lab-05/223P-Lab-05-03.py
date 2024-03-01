# Write a Python program that performs the following operations on a dictionary:

# Create an empty dictionary called my_dict.
# Add the key-value pairs "name" with the value "Maximus", "age" with the value 25, and "city" with the value "New York" to my_dict.
# Display the keys of the dictionary.
# Check if the key "age" is present in the dictionary. If it is, print "Age is present" along with its value.
# Update the value of "age" to 26.
# Delete the key-value pair with the key "city" from the dictionary.
# Display the final contents of the dictionary.

my_dict = {}
print("Empty Dictionary: ")
print(my_dict)

#add key value pairs
my_dict["name"] = 'Maximus'
my_dict["age"] = 25 
my_dict["city"] = 'New York'
print(my_dict)

print("Keys of the dictionary:", my_dict.keys())

if "age" in my_dict:
    print("Age is present", my_dict["age"])
    
my_dict["age"] = 26

del my_dict["city"]

print("Final contents of the dictionary", my_dict)   
