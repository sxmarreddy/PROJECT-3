
def add_expense(expenses):
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transportation, entertainment): ")
    
    expense = {
        'amount': amount,
        'description': description,
        'category': category
    }
    
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
    else:
        print("\n--- Your Expenses ---")
        for i, expense in enumerate(expenses, 1):
            print(f"{i}. Amount: ${expense['amount']:.2f}, Description: {expense['description']}, Category: {expense['category']}")
        print()

def main():
    expenses = []
    
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
