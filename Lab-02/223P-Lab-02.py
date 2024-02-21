def filter_numbers(numbers):
    even = [num for num in numbers if num % 2 == 0]

    if len(even) > 5:
        print("The length of the even numbers list exceeds 5.")
    elif len(even) == 5:
        print("The length of the even numbers list is the same as 5.")
    else:
        print("The length of the even numbers list is less than 5.")

    return even

# Example input
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = filter_numbers(input_numbers)
print(filtered_numbers)
