
# __init__ is the setup phase. It runs automatically every time you create a new bank account object.
# Self = It refers to the specific object being created. Think of it as "this particular account." 
# It's how Python knows to assign "Alice" to Alice's account and "Bob" to Bob's account, keeping them separate.
# An attribute is a variable or a function attached to an object that holds its data (like .balance) or defines its behavior (like .deposit)

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

check = 0
while(True):
    print("\n=========Welcome to the bank============\n")
    print("1. Create a bank account.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Check Balance.")
    print("0. Exit.")
   
    user_choice = int(input("Enter: "))
    match user_choice:
        case 1:
            check += 1
            if(check > 1):
                print("You can only create only one account at a time")
            else:
                name = input("Enter your holder's name: ")
                amount = int(input("Enter the balance: "))
                user_account = BankAccount(name, amount)
        case 2: 
            if(check == 0):
                print("Please create an account first.")
            else: 
                print(f"\n{user_account.holder}'s Account")
                depo_amount = int(input("Enter the amount: "))
                user_account.deposit(depo_amount)
                print("Current balance: ", user_account.balance)
        case 3:
            if(check == 0):
                print("Please create an account first.")
            else:
                print(f"\n{name}'s Account")
                withd_amount = int(input("Enter the amount: "))
                user_account.withdraw(withd_amount)
                print("Current balance: ", user_account.balance)
        case 4:
            if(check == 0):
                print("Please create an account first.")
            else:
                print("Your current balance: ", user_account.balance)
        case 0:
            print("\nThank you for using.")
            break
        case _:
            print("\nEnter from the valid input.")