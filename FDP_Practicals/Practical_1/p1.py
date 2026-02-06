print("Finance Tracker \n 1.Income \n 2.Expense \n 3.Balance \n 4.Exit")

def summary():
    income = 0
    expense = 0

    with open("balance.txt","r") as f:
        for line in f:
            entry_type, amount = line.split(":")
            amount = float(amount)

            if entry_type.strip() == "Income":
                income += amount
            elif entry_type == "Expense":
                expense += amount

    balance = income - expense
    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Current Balance: {balance}")

while True:
    o = int(input("Enter Operation (1/2/3/4): "))

    if o == 1:
        income = float(input("Enter Income: "))
        with open("balance.txt","a") as f:
            f.write(f"Income: {income}\n")
        print(f"Income {income} added.")

    elif o == 2:
        expense = float(input("Enter Expense: "))
        with open("balance.txt","a") as f:
            f.write(f"Expense: {expense}\n")
        print(f"Expense {expense} added.")

    elif o == 3:
        summary()

    elif o == 4:
        print("Exiting Finance Tracker.")
        break

    else:
        print("Invalid")
