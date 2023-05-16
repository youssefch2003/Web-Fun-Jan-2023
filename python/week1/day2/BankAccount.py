class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
        # your code here
    def withdraw(self, amount):
        # your code here
        if self.balance>0 :
            self.balance-= amount
        else:
            print("Insufficient funds: Charging a $5 fee" )
            self.balance-= 5
        return self
    def display_account_info(self):
        # your code here
        print("balance:$",self.balance)
        return self
        
    def yield_interest(self):
        # your code here
        if self.balance > 0 :
            self.balance+=(self.balance * self.int_rate)
        return self
    @classmethod
    def printall(cls):
        for account in cls.accounts :
            cls.display_account_info(account)

yassin=BankAccount(0.05,150)
ahmed=BankAccount(0.10,1000)

yassin.display_account_info().deposit(50).deposit(70).deposit(80).withdraw(50).yield_interest().display_account_info()
ahmed.deposit(50).deposit(50).withdraw(100.1).withdraw(50.5).withdraw(33.3).withdraw(200).yield_interest().display_account_info()

#BONUS
print("NINJA BONUS")
BankAccount.printall()
