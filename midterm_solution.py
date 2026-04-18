# Ask for student name
student_name = input("Student name: ")

# Validate weekly budget input
weekly_budget = 0
budget_is_valid = False

while budget_is_valid == False:
    weekly_budget_input = input("Weekly budget: ")

    if weekly_budget_input == "":
        print("Invalid input. Enter a number.")
    else:
        is_number = True
        index_counter = 0

        while index_counter < len(weekly_budget_input):
            if weekly_budget_input[index_counter] < '0' or weekly_budget_input[index_counter] > '9':
                is_number = False
            index_counter = index_counter + 1

        if is_number == True:
            weekly_budget = int(weekly_budget_input)
            budget_is_valid = True
        else:
            print("Invalid input. Enter numbers only.")

# Categories (hardcoded)
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

print("")
print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

index_counter = 0
while index_counter < 5:
    print(" " + str(index_counter + 1) + ". " + category_names[index_counter] + "       [e.g. " + category_examples[index_counter] + "]")
    index_counter = index_counter + 1

print("==========================================")

# Storage
expense_category_list = []
expense_description_list = []
expense_amount_list = []
expense_alert_list = []

entry_counter = 1

while entry_counter <= 4:
    print("")
    print("--- EXPENSE " + str(entry_counter) + " ---")

    valid_category = False
    category_number = 0

    # Category validation
    while valid_category == False:
        category_input = input("Category (0 to skip): ")

        if category_input == "":
            print("Invalid input.")
        else:
            is_number = True
            index_counter = 0

            while index_counter < len(category_input):
                if category_input[index_counter] < '0' or category_input[index_counter] > '9':
                    is_number = False
                index_counter = index_counter + 1

            if is_number == True:
                category_number = int(category_input)

                if category_number >= 0 and category_number <= 5:
                    valid_category = True
                else:
                    print("Enter number from 0 to 5.")
            else:
                print("Numbers only.")

    if category_number == 0:
        entry_counter = entry_counter + 1
    else:
        description_text = input("Description: ")

        valid_amount = False
        amount_value = 0

        # Amount validation
        while valid_amount == False:
            amount_input = input("Amount: ")

            if amount_input == "":
                print("Invalid input.")
            else:
                is_number = True
                index_counter = 0

                while index_counter < len(amount_input):
                    if amount_input[index_counter] < '0' or amount_input[index_counter] > '9':
                        is_number = False
                    index_counter = index_counter + 1

                if is_number == True:
                    amount_value = int(amount_input)
                    valid_amount = True
                else:
                    print("Numbers only.")

        # Check 25% rule
        high_expense_limit = weekly_budget * 0.25
        alert_message = ""

        if amount_value > high_expense_limit:
            alert_message = "! High Expense Alert!"

        # Store data
        expense_category_list.append(category_number)
        expense_description_list.append(description_text)
        expense_amount_list.append(amount_value)
        expense_alert_list.append(alert_message)

        entry_counter = entry_counter + 1

# Compute totals
total_spent = 0
index_counter = 0

while index_counter < len(expense_amount_list):
    total_spent = total_spent + expense_amount_list[index_counter]
    index_counter = index_counter + 1

remaining_balance = weekly_budget - total_spent

if remaining_balance >= 0:
    budget_status = "Budget OK! Keep it up."
else:
    budget_status = "Overspent! Reduce spending."

# Output report
print("")
print("======================================================")
print("     " + student_name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")

print("  Weekly Budget  : P" + str(weekly_budget))

index_counter = 0

while index_counter < len(expense_category_list):
    category_index = expense_category_list[index_counter] - 1

    print("  [" + str(index_counter + 1) + "] " + category_names[category_index])
    print("      " + expense_description_list[index_counter] + "    P" + str(expense_amount_list[index_counter]) + " " + expense_alert_list[index_counter])

    index_counter = index_counter + 1

print("------------------------------------------------------")
print("  Total Spent    : P" + str(total_spent))
print("  Remaining      : P" + str(remaining_balance))
print("  Status         : " + budget_status)
print("======================================================")
