student_name = ""
while student_name == "":
    student_name = input("Enter your name: ")
    if student_name.replace(" ", "") == "":
        print("Name cannot be blank. Please enter again.")


weekly_budget = -1
while weekly_budget <= 0:
    budget_input = input("Enter your weekly budget: ")
    if budget_input == "":
        print("Invalid input. Enter a number.")
    else:
        is_valid_number = True
        index_counter = 0
        while index_counter < len(budget_input):
            if budget_input[index_counter] < '0' or budget_input[index_counter] > '9':
                is_valid_number = False
            index_counter = index_counter + 1

        if is_valid_number == True:
            weekly_budget = int(budget_input)
            if weekly_budget <= 0:
                print("Budget must be greater than zero.")
        else:
            print("Invalid input. Enter a valid number.")


print("\n==========================================")
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

index_counter = 0
while index_counter < 5:
    print(" " + str(index_counter + 1) + ". " + category_names[index_counter] + "       [e.g. " + category_examples[index_counter] + "]")
    index_counter = index_counter + 1

print("==========================================")


expense_count = 0
expense_category_list = []
expense_description_list = []
expense_amount_list = []
expense_alert_list = []


entry_number = 1
while entry_number <= 4:
    print("\n--- EXPENSE " + str(entry_number) + " ---")

    category_number = -1
    while category_number < 0 or category_number > 5:
        category_input = input("Category (0 to skip): ")

        if category_input == "":
            print("Invalid input.")
        else:
            is_valid_number = True
            index_counter = 0
            while index_counter < len(category_input):
                if category_input[index_counter] < '0' or category_input[index_counter] > '9':
                    is_valid_number = False
                index_counter = index_counter + 1

            if is_valid_number == True:
                category_number = int(category_input)
            else:
                print("Invalid input.")

    if category_number == 0:
        entry_number = entry_number + 1
    else:
        description_text = ""
        while description_text == "":
            description_text = input("Description: ")
            if description_text.replace(" ", "") == "":
                print("Description cannot be blank.")

        amount_value = -1
        while amount_value < 0:
            amount_input = input("Amount: ")
            if amount_input == "":
                print("Invalid input.")
            else:
                is_valid_number = True
                index_counter = 0
                while index_counter < len(amount_input):
                    if amount_input[index_counter] < '0' or amount_input[index_counter] > '9':
                        is_valid_number = False
                    index_counter = index_counter + 1

                if is_valid_number == True:
                    amount_value = int(amount_input)
                else:
                    print("Invalid input.")

       
        high_limit = weekly_budget * 0.25
        alert_text = ""
        if amount_value > high_limit:
            alert_text = "! High Expense Alert!"

        
        expense_category_list.append(category_names[category_number - 1])
        expense_description_list.append(description_text)
        expense_amount_list.append(amount_value)
        expense_alert_list.append(alert_text)

        expense_count = expense_count + 1
        entry_number = entry_number + 1


total_spent = 0
index_counter = 0
while index_counter < expense_count:
    total_spent = total_spent + expense_amount_list[index_counter]
    index_counter = index_counter + 1

remaining_balance = weekly_budget - total_spent

status_text = ""
if remaining_balance >= 0:
    status_text = "Budget OK! Keep it up."
else:
    status_text = "Overspent! Reduce spending."


print("\n======================================================")
print("     " + student_name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")
print("  Weekly Budget  : P" + str(weekly_budget))

index_counter = 0
while index_counter < expense_count:
    print("  [" + str(index_counter + 1) + "] " + expense_category_list[index_counter])
    print("      " + expense_description_list[index_counter] + "    P" + str(expense_amount_list[index_counter]) + "  " + expense_alert_list[index_counter])
    index_counter = index_counter + 1

print("------------------------------------------------------")
print("  Total Spent    : P" + str(total_spent))
print("  Remaining      : P" + str(remaining_balance))
print("  Status         : " + status_text)
print("======================================================")
