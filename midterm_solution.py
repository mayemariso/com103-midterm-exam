student_name = input("Student name: ")

weekly_budget = 0
valid_budget = False
while not valid_budget:
    budget_input = input("Weekly budget: ")
    valid_budget = True
    for character in budget_input:
        if character != '.' and not ('0' <= character <= '9'):
            valid_budget = False
    if valid_budget and budget_input != '':
        weekly_budget = float(budget_input)
    else:
        valid_budget = False
        print("Invalid input. Please enter a valid number.")

print()
print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

category_names = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

category_examples = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi top-up",
    "Notebook, pen, bond paper",
    "Games, movies, hangout"
]

category_index = 0
while category_index < 5:
    category_number = category_index + 1
    category_label = category_names[category_index]
    category_example = category_examples[category_index]
    print(f" {category_number}. {category_label:<22} [e.g. {category_example}]")
    category_index = category_index + 1

print("==========================================")
print()

logged_expense_categories = []
logged_expense_descriptions = []
logged_expense_amounts = []

total_number_of_expenses = 4
high_expense_threshold = weekly_budget * 0.25

expense_slot = 1
while expense_slot <= total_number_of_expenses:
    print(f"--- EXPENSE {expense_slot} ---")

    valid_category = False
    chosen_category_number = 0
    while not valid_category:
        category_input = input("Category (0 to skip): ")
        is_digit = True
        for character in category_input:
            if not ('0' <= character <= '9'):
                is_digit = False
        if is_digit and category_input != '':
            chosen_category_number = int(category_input)
            if chosen_category_number == 0 or (1 <= chosen_category_number <= 5):
                valid_category = True
            else:
                print("Invalid category. Please enter a number from 0 to 5.")
        else:
            print("Invalid input. Please enter a number from 0 to 5.")

    if chosen_category_number == 0:
        print()
        expense_slot = expense_slot + 1
        continue

    expense_description = input("Description: ")

    valid_amount = False
    expense_amount = 0
    while not valid_amount:
        amount_input = input("Amount: ")
        valid_amount = True
        for character in amount_input:
            if character != '.' and not ('0' <= character <= '9'):
                valid_amount = False
        if valid_amount and amount_input != '':
            expense_amount = float(amount_input)
        else:
            valid_amount = False
            print("Invalid input. Please enter a valid amount.")

    logged_expense_categories.append(category_names[chosen_category_number - 1])
    logged_expense_descriptions.append(expense_description)
    logged_expense_amounts.append(expense_amount)

    print()
    expense_slot = expense_slot + 1

total_amount_spent = 0
amount_index = 0
while amount_index < len(logged_expense_amounts):
    total_amount_spent = total_amount_spent + logged_expense_amounts[amount_index]
    amount_index = amount_index + 1

remaining_balance = weekly_budget - total_amount_spent

if remaining_balance >= 0:
    budget_status = "Budget OK! Keep it up."
else:
    budget_status = "Overspent! Reduce spending."

student_name_upper = student_name.upper()

print("======================================================")
print(f"     {student_name_upper} -- WEEKLY EXPENSE LOG")
print("======================================================")

weekly_budget_whole = int(weekly_budget)
weekly_budget_cents = int(round((weekly_budget - weekly_budget_whole) * 100))
if weekly_budget_cents < 10:
    weekly_budget_formatted = f"P{weekly_budget_whole}.0{weekly_budget_cents}"
else:
    weekly_budget_formatted = f"P{weekly_budget_whole}.{weekly_budget_cents}"

print(f"  Weekly Budget  : {weekly_budget_formatted}")

log_index = 0
while log_index < len(logged_expense_categories):
    entry_number = log_index + 1
    entry_category = logged_expense_categories[log_index]
    entry_description = logged_expense_descriptions[log_index]
    entry_amount = logged_expense_amounts[log_index]

    entry_amount_whole = int(entry_amount)
    entry_amount_cents = int(round((entry_amount - entry_amount_whole) * 100))
    if entry_amount_cents < 10:
        entry_amount_formatted = f"P{entry_amount_whole}.0{entry_amount_cents}"
    else:
        entry_amount_formatted = f"P{entry_amount_whole}.{entry_amount_cents}"

    if entry_amount > high_expense_threshold:
        high_expense_tag = "  ! High Expense Alert!"
    else:
        high_expense_tag = ""

    print(f"  [{entry_number}] {entry_category}")
    print(f"      {entry_description:<36}{entry_amount_formatted}{high_expense_tag}")

    log_index = log_index + 1

print("------------------------------------------------------")

total_whole = int(total_amount_spent)
total_cents = int(round((total_amount_spent - total_whole) * 100))
if total_cents < 10:
    total_formatted = f"P{total_whole}.0{total_cents}"
else:
    total_formatted = f"P{total_whole}.{total_cents}"

remaining_absolute = remaining_balance
if remaining_balance < 0:
    remaining_absolute = -remaining_balance

remaining_whole = int(remaining_absolute)
remaining_cents = int(round((remaining_absolute - remaining_whole) * 100))
if remaining_cents < 10:
    if remaining_balance < 0:
        remaining_formatted = f"-P{remaining_whole}.0{remaining_cents}"
    else:
        remaining_formatted = f"P{remaining_whole}.0{remaining_cents}"
else:
    if remaining_balance < 0:
        remaining_formatted = f"-P{remaining_whole}.{remaining_cents}"
    else:
        remaining_formatted = f"P{remaining_whole}.{remaining_cents}"

print(f"  Total Spent    : {total_formatted}")
print(f"  Remaining      : {remaining_formatted}")
print(f"  Status         : {budget_status}")
print("======================================================")
