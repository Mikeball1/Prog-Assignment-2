class accounts:
  def __init__ (self,accountNumber,currentBalance):
   self.accountNumber=accountNumber
   self.balance=currentBalance
   #self.rateOfinterest=rateOfinterest
  def getAccountNumber(self):
   accNumber=input("What is your account number?")
   return accNumber
  def getAccountHolderName(self):
   accHolderName=input("What is your Name")
  # def getRateOfInterest():
  # =input("")
  def getCurrentBalance(self):
   bal=input("")
  #  deposit=input("")
  #  withdraw=input("")
  def deposit():
    acc1.balance+=int(input("How much would you like to deposit"))
    return acc1.balance
    

class program(accounts):
  def __init__(self,accountsNumber,currentBalance):
    super().__init__(accountsNumber,currentBalance)
  def showMainMenu(self):
    choice=input("Which option would you like to choose:\n1.Open Account\n2.Select Account\n3.Exit\n")
    return choice
  def showAccountMenu(self,number):
     choice2=input("Which option would you like to choose:\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account")
     return choice2
# class showAccountMenu:
#     def checkbal():
#     def deposit():
#     def withdraw():
#     def exitacc():

obj=program(1,2)

match obj.showMainMenu():
 case '1':
  obj.getAccountHolderName()
  obj.getCurrentBalance()
 case '2':
  match obj.showAccountMenu(obj.getAccountNumber()):
    case '1':
      print(obj.accountNumber)
    case '2':
      obj.deposit
 case '3':
  pass




# class showMainMenu:


# #   def __init__(self,OpenAcc,SelectAcc,Exit):
# #     self.openacc=OpenAcc
# #     self.selectacc=SelectAcc
# #     self.exit=Exit
# class showAccountMenu:
# #  def __init__(self,CheckBal,deposit,withdraw,exitacc):
# #     self.checkbal=CheckBal
# #     self.deposit=deposit
# #     self.withdraw=withdraw
# #     self.exitacc=exitacc