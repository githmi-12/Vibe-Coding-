def get_valid_amount(prompt, max_limit=float('inf'), allow_done=False):
    while True:
        user_input = input(prompt).strip()
        
        # Check for 'done' if allowed for this input
        if allow_done and user_input.lower() == "done":
            return "done"
            
        # Constraint: Cannot be null/empty
        if not user_input:
            print("Input cannot be empty. Please enter a value.")
            continue
            
        try:
            # Constraint: Cannot be letters (unless it was 'done' handled above)
            value = float(user_input)
            
            # Constraint: Cannot be negative
            if value < 0:
                print("Value cannot be negative. Please re-enter.")
                continue
            
            # Constraint: Cannot exceed 2 dp
            if "." in user_input and len(user_input.split(".")[1]) > 2:
                print("Value cannot exceed 2 decimal places. Please re-enter.")
                continue

            # Constraint: Expense cannot be higher than total budget
            if value > max_limit:
                print("Expense cannot be higher than the total monthly budget")
                continue
                
            return value
            
        except ValueError:
            print("Invalid input. Please enter a numeric value in LKR or 'done' to finish.")

def main():
    # 1. Get Total Monthly Budget
    budget = get_valid_amount("Please enter the total monthly budget in LKR including cents: ")
    
    expenses = []
    
    # 2. Collect Multiple Expenses
    while True:
        count = len(expenses) + 1
        prompt = f"Please enter expense {count} in LKR (or 'done' to finish): "
        
        # Allow 'done' only if they have at least one expense > 0
        can_finish = len(expenses) > 0 and any(e > 0 for e in expenses)
        
        result = get_valid_amount(prompt, max_limit=budget, allow_done=True)
        
        if result == "done":
            if can_finish:
                break
            else:
                print("You must enter at least one expense greater than zero before finishing.")
                continue
        
        expenses.append(result)

    # 3. Calculations
    total_expenses = sum(expenses)
    remaining_balance = budget - total_expenses
    
    # 4. Output Logic
    if remaining_balance < 0:
        print("Monthly budget is insufficient for these expenses!")
    else:
        if remaining_balance < 500:
            print("Warning: Low Funds")
            
        print(f"Remaining balance in LKR: {remaining_balance:.2f}")

if __name__ == "__main__":
    main()