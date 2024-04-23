# Write a Python program that calculates the number of days between two given dates. Your program should take two input dates in the format "YYYY-MM-DD" and output the number of days between them. Ensure that your program handles invalid inputs gracefully.

# NOTE : Use the function days_between_dates() to find out the difference.

import datetime


def days_between_dates(date1, date2):
    try:
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()

        delta = d2 - d1
        return abs(delta.days)
    except ValueError as e:
        return f"Invalid date format"


if __name__ == "__main__":
    data_input_1 = input("Enter the first date (YYYY-MM-DD): ")
    data_input_2 = input("Enter the second date (YYYY-MM-DD): ")

    result = days_between_dates(data_input_1, data_input_2)
    print(f"Number of days between dates: {result}")