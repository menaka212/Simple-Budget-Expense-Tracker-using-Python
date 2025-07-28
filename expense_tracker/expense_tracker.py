import os

FILENAME = "expenses.txt"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport, Utilities): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    
    with open(FILENAME, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")
    
    print("✅ Expense added successfully!\n")

def view_expenses():
    print("\n📋 All Expenses:\n")
    if not os.path.exists(FILENAME):
        print("No expenses found.\n")
        return
    
    with open(FILENAME, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            print(f"Date: {date} | Category: {category} | Amount: ₹{amount} | Description: {description}")
    print()

def monthly_summary():
    if not os.path.exists(FILENAME):
        print("No expenses found.\n")
        return

    month = input("Enter month (YYYY-MM): ")
    total = 0

    print(f"\n📅 Monthly Summary for {month}:\n")
    with open(FILENAME, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            if date.startswith(month):
                print(f"Date: {date} | Category: {category} | Amount: ₹{amount} | Description: {description}")
                total += float(amount)
    
    print(f"\n💰 Total Spent in {month}: ₹{total}\n")

def main():
    while True:
        print("==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
