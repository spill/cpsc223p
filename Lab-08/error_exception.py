def divide_numbers(num1, num2):
    try:

        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both inputs must be numbers.")


        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")


        return num1 / num2

    except TypeError as e:

        raise TypeError(f"Handling error due to incorrect input types: {e}")

    except ZeroDivisionError as e:

        raise ZeroDivisionError(f"Handling error due to division by zero: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

try:
    print(divide_numbers(10, 2)) 
except Exception as e:
    print(e)

try:
    print(divide_numbers("a", 2))  
except Exception as e:
    print(e)

try:
    print(divide_numbers(10, 0))  
except Exception as e:
    print(e)

try:
    print(divide_numbers(10, "b")) 
except Exception as e:
    print(e)
