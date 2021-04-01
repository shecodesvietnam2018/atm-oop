class ATM:
    def __init__(self):
        self.balance = 10000
        self.limit = 10000000
        self.history = []

    def deposit(self, amount):
        if amount + self.balance > self.limit:
            raise Exception("Limit exceeded")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Balance cannot be negative")
        self.balance = self.balance - amount

    def display_history(self):
        print("History:")
        for content in self.history:
            print(content)


atm = ATM()
while True:
    print(f"Current balance: {atm.balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display history")
    print("4. Exit")
    selection = int(input("Your selection: "))
    while selection != 1 and selection != 2 and selection != 3 and selection != 4:
        selection = int(input("Your selection: "))
    try:
        if selection == 1:
            amount = int(input("How much money do you want to deposit? "))
            atm.deposit(amount)
        elif selection == 2:
            amount == int(input("How much money do you want to withdraw? "))
            atm.withdraw(amount)
        elif selection == 3:
            atm.display_history()
        else:
            break
    except Exception as e:
        print(e)
    finally:
        print()  # New line on the screen
