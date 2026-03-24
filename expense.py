def add_expense():
    categories = ["Food", "Travel", "Shopping"]

    category = input("Enter category (Food/Travel/Shopping): ").capitalize()

    if category not in categories:
        print(" Invalid category! Choose from Food, Travel, Shopping.")
        return

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(" Invalid amount! Please enter a number.")
        return

    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount}\n")

    print(" Expense added successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            print("\n----- All Expenses -----")
            for line in file:
                category, amount = line.strip().split(",")
                print(f"Category: {category} | Amount: ₹{amount}")
    except FileNotFoundError:
        print("No expense file found. Add expenses first.")


def calculate_total():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                total += float(amount)

        print(f"\n Total Expense: ₹{total}")
    except FileNotFoundError:
        print(" No expense file found.")


def category_count():
    counts = {}

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                counts[category] = counts.get(category, 0) + 1

        print("\n Category-wise Count:")
        for cat, count in counts.items():
            print(f"{cat}: {count} times")

    except FileNotFoundError:
        print(" No expense file found.")

while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category-wise Count")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        category_count()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print(" Invalid choice! Try again.")