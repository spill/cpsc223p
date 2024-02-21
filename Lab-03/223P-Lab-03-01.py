def expense_calculation(hotel_cost=0, food_cost=0, entertainment_cost=0, extra_expenses=0):
    total_expense = hotel_cost + food_cost + entertainment_cost + extra_expenses
    return total_expense
    
    #Example
total_cost = expense_calculation(hotel_cost=200, food_cost=150, entertainment_cost=100, extra_expenses=50)
print("Total expense: $", total_cost)