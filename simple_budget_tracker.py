def get_valid_amount(prompt, max_limit=float('inf')):
    while True:
        try:
            value_str = input(prompt).strip()
            
            # Constraint: Cannot be null/empty
            if not value_str:
                print("Input cannot be empty. Please enter a value.")
                continue
            
            # Constraint: Cannot be letters
            value = float(value_str)
            
            # Constraint: Cannot be negative
            if value < 0:
                print("Value cannot be negative. Please re-enter.")
                continue
            
            # Constraint: Cannot exceed 2 dp
            if "." in value_str and len(value_str.split(".")[1]) > 2:
                print("Value cannot exceed 2 decimal places. Please re-enter.")
                continue

            # Constraint: Expense cannot be higher than total budget
            if value > max_limit:
                print("Expense cannot be higher than the total monthly budget")
                continue
                
            return value
            
        except ValueError:
            print("Invalid input. Please enter a numeric value in LKR.")

def main():
    # 1. Total Monthly Budget
    budget = get_valid_amount("Please enter the total monthly budget in LKR including cents: ")
    
    # 2. Get 3 Expenses
    expenses = []
    prompts = [
        "Please enter the first expense in LKR: ",
        "Please enter the second expense in LKR: ",
        "Please enter the third expense in LKR: "
    ]
    
    for p in prompts:
        expense = get_valid_amount(p, max_limit=budget)
        expenses.append(expense)
    
    # 3. Calculations
    total_expenses = sum(expenses)
    remaining_balance = budget - total_expenses
    
    # 4. Output Logic
    if remaining_balance < 0:
        print("Monthly budget is insufficient for these expenses!")
    else:
        # Task 02 Addition: Warning for low funds
        if remaining_balance < 500:
            print("Warning: Low Funds")
            
        print(f"Remaining balance in LKR: {remaining_balance:.2f}")

if __name__ == "__main__":
    main()