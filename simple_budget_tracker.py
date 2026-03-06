def get_valid_amount(prompt, max_limit=float('inf'), is_budget=False):
    while True:
        try:
            value_str = input(prompt).strip()
            
            # Check if input is empty
            if not value_str:
                print("Input cannot be empty. Please enter a value.")
                continue
            
            value = float(value_str)
            
            # Constraint: Cannot be negative
            if value < 0:
                print("Value cannot be negative. Please re-enter.")
                continue
            
            # Constraint: Cannot exceed 2 decimal places
            if "." in value_str and len(value_str.split(".")[1]) > 2:
                print("Value cannot exceed 2 decimal places. Please re-enter.")
                continue

            # Constraint: Expense cannot exceed total budget
            if value > max_limit:
                print("Expense cannot be higher than the total monthly budget")
                continue
                
            return value
            
        except ValueError:
            print("Invalid input. Please enter a numeric value in LKR.")

def main():
    # 1. Get Total Budget
    budget = get_valid_amount("Please enter the total monthly budget in LKR including cents: ", is_budget=True)
    
    # 2. Get 3 Expenses
    expenses = []
    prompts = [
        "Please enter the first expense in LKR: ",
        "Please enter the second expense in LKR: ",
        "Please enter the third expense in LKR: "
    ]
    
    for p in prompts:
        # Pass the 'budget' as the max_limit to satisfy the constraint
        expense = get_valid_amount(p, max_limit=budget)
        expenses.append(expense)
    
    # 3. Calculations
    total_expenses = sum(expenses)
    remaining_balance = budget - total_expenses
    
    # 4. Output
    if remaining_balance < 0:
        print("Monthly budget is insufficient for these expenses!")
    else:
        # Display balance formatted to 2 decimal places
        print(f"Remaining balance in LKR: {remaining_balance:.2f}")

if __name__ == "__main__":
    main()