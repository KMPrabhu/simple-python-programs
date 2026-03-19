accounts = {}

def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter initial deposit: "))
    accounts[name] = balance
    print("Account created successfully!")

def deposit():
    name = input("Enter name: ")
    if name in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[name] += amount
        print("Amount deposited!")
    else:
        print("Account not found!")

def withdraw():
    name = input("Enter name: ")
    if name in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[name] >= amount:
            accounts[name] -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance():
    name = input("Enter name: ")
    if name in accounts:
        print("Balance:", accounts[name])
    else:
        print("Account not found!")

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Balance 5.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        break
    else:
        print("Invalid choice")
