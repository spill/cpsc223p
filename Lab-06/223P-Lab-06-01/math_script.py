import math_operations

def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    sum = math_operations.add(x, y)
    print(f"{x} + {y} is {sum}")

    subtraction = math_operations.subtract(x, y)
    print(f"{x} - {y} is {subtraction}")



if __name__ == "__main__":
    main()