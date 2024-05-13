class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            return "Invalid: Requires numbers to do addition"
    def subtract(self, a, b):
        try:
            return a - b
        except TypeError:
                return "Invalid: Requires numbers to do subtraction"
    def multiply(self, a, b):
        try:
            return a * b
        except TypeError:
            return "Invalid: requires numbers to do multiplication"
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Invalid: Division by Zero is undefined"
        except TypeError:
            return "Invalid: requires numbers to do division"

#Example numbers
calculate = Calculator()

print(calculate.add(9, 7)) # Answer: 16
print(calculate.add("z", 5)) # Invalid: requires numbers to addition
print(calculate.subtract(30, 2)) # Answer: 28
print(calculate.multiply(10, 2)) # Answer: 20
print(calculate.divide(4, 0)) # Invalid: Division by Zero is undefined
print(calculate.divide(10, 2)) # Answer: 5.0