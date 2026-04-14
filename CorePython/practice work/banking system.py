class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.count = 0 #withdrawl count
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,amount):
        if self.count >= 3:
            print("limit reached")
        elif amount > 20000:
            print ("you cannot withdraw more than 20k")
        elif self.balance - amount < 1000:
            print("minimum balance should be 1000rs")
        else:
            self.balance=self.balance - amount
            self.count +=1
            print ("withdraw succesful")
            print ("balance",self.balance)

acc = BankAccount(50000)
acc.withdraw(10000)
acc.withdraw(1500)
acc.withdraw(1500)
acc.withdraw(20)
