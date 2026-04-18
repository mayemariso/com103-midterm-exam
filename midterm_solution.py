
categories = {
    1: "Food & Drinks",
    2: "Transportation",
    3: "Mobile / Internet",
    4: "School Supplies",
    5: "Entertainment"
}


print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
for key, value in categories.items():
    print(f" {key}. {value}")
print("==========================================\n")


name = input("Enter your name: ")
weekly_budget = float(input("Enter your weekly budget: "))


expenses = []
total_spent = 0
threshold = weekly_budget * 0.25

for i in range(1, 5):
    print(f"\n--- EXPENSE {i} ---")
    category = int(input("Category (0 to skip): "))
    if category == 0:
        continue
    if category not in categories:
        print("Invalid category. Skipping this entry.")
        continue

    description = input("Description: ")
    amount = float(input("Amount: "))
    high_expense = "! High Expense Alert!" if amount > threshold else ""
    expenses.append((categories[category], description, amount, high_expense))
    total_spent += amount


remaining_balance = weekly_budget - total_spent
status = "Budget OK! Keep it up." if remaining_balance >= 0 else "Overspent! Reduce spending."


print("\n======================================================")
print(f"     {name.upper()} -- WEEKLY EXPENSE LOG")
print("======================================================")
print(f"  Weekly Budget  : P{weekly_budget:.2f}")
for idx, (category, description, amount, high_expense) in enumerate(expenses, start=1):
    print(f"  [{idx}] {category}")
    print(f"      {description:<30} P{amount:.2f} {high_expense}")
print("------------------------------------------------------")
print(f"  Total Spent    : P{total_spent:.2f}")
print(f"  Remaining      : P{remaining_balance:.2f}")
print(f"  Status         : {status}")
print("======================================================")
