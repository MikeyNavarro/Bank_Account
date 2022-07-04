class BankAccount: 
  bank_Name = "Coding_Credit_Union"
  
  def __init__(self, first_name, last_name, age , interestRate=0.01 , balance = 0 ):

    self.first_name = first_name
    self.last_name = last_name 
    self.age = age
    self.interestRate = interestRate
    self.balance = balance

  def deposit_Amount(self, deposit_Amount):
    self.balance += deposit_Amount
    return self 
  
  def withdraw_Amount(self, withdraw_Amount):
    self.balance -= withdraw_Amount
    return self 

  def total_Balance(self):
    print(self.balance)
    return self 
  

  def accountInfo(self):
    print(self.bank_Name)
    print(self.first_name)
    print(self.last_name)
    print(self.age)
    print(self.interestRate)
    return self
  
  def yeiledInterest(self):
    self.balance = (self.balance * self.interestRate) + self.balance 
    return self

user1 = BankAccount("Mikey", "Navarro" , 22 , 0.01 )
user2 = BankAccount("Mikaela", "Navarro", 24, 0.01) 

user1.deposit_Amount(50).deposit_Amount(5).deposit_Amount(500).withdraw_Amount(250).yeiledInterest().total_Balance()
user2.deposit_Amount(500).deposit_Amount(5).withdraw_Amount(250).withdraw_Amount(25).withdraw_Amount(25).yeiledInterest().total_Balance()

