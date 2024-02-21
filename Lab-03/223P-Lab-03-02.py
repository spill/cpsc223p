def inputted_list():
    inputted_string = input("Enter a list of numbers separate by a space: ")
    user_list = inputted_string.split() #splits the string into a list of substrings through split()
    
    return list(map(int, user_list)) # converts every argument into an int and returns

if __name__ == "__main__":
    numbers = inputted_list()
    squared_numbers = list(map(lambda x: x**2, numbers))
    print("List of squared numbers:", squared_numbers)