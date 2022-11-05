print("------ATM Project------")
class bank_account():
    def __init__(self, owner):
        self.owner = owner
        self.balance = 1500.0
        self.password = "123456"

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

    def login(self, password):
        if password == self.password:
            print("Login successful")
            return True
        else:
            print("Incorrect PIN")
            return False

    def deposit(self):
        deposit = float(input("Enter amount you want to deposit: "))
        if deposit >= 0:
            print(f"You have successfully deposited ${self.deposit}")
        else:
            print("You cannot deposit this amount")
        self.balance += deposit
        print(f"You now have {self.balance} in your account")

    def withdraw(self):
        withdraw = float(input("Enter amount you want to withdraw: "))
        if withdraw <= self.balance:
            print(f"You have successfully withdrawn ${withdraw}")
        else: 
            withdraw = float(input("This amount exceeds your balance. Enter a different value: "))
        self.balance -= withdraw
        print(f"You now have {self.balance} in your account")

    def check_balance(self):
        print(f"Your balance is currently: {self.balance}")

    def quit(self):
        return False

a = bank_account("Zana Hashani")
password = str(input("Enter your PIN: "))
success = a.login(password)
while True:
    if(success):
        action = input("Do you want to withdraw (W), deposit (D), check your balance (B), or quit (Q)? ")
        if action == "W":
            a.withdraw()
            print(action)
        elif action == "D":
            a.deposit()
            print(action)
        elif action == "B":
            a.check_balance()
            print(action)
        elif action == "Q":
            a.quit()
            break
print("------Zana Hashani------")