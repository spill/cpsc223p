# Write a Python program that prompts the user to enter their name and age. Then, use the string.Template module to create a personalized message with the user's name and age.

# Additionally, log this personalized message using the logging module with the level set to INFO.

 

# NOTE: Try to keep the program very straightforward. No unnecessary functions needed.

import logging
from string import Template

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

username = input("Enter your name: ")
age = input("Enter your age:")

template_string = Template("Hello $name, you are $age years old.")

message = template_string.substitute(name=username, age=age)

logging.info(message)
print(message)