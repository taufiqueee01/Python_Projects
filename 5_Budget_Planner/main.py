def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val < 0: print("Value cannot be negative.")
            else: return val
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("--- Budget & Savings Planner ---")
    
    income = get_float("Enter Monthly Income: ")
    goal = get_float("Enter Total Savings Goal: ")
    
    expenses = []
    print("\nEnter Expenses (type 'done' to finish):")
    
    while True:
        name = input("Expense Name (or 'done'): ")
        if name.lower() == 'done': break
        cost = get_float(f"Cost for {name}: ")
        expenses.append(cost)
        
    total_expenses = sum(expenses)
    savings = income - total_expenses
    
    print("\n--- Financial Summary ---")
    print(f"Total Income: ${income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Monthly Savings: ${savings}")
    
    if savings <= 0:
        print("Warning: You are spending more than or equal to what you earn.")
        print("You cannot reach your goal with current habits.")
    else:
        months_needed = goal / savings
        print(f"\nTime to reach goal (${goal}):")
        print(f"Approximately {round(months_needed, 1)} months")

if __name__ == "__main__":
    main()
