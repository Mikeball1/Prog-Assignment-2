class program:
  def showMainMenu():
    choice=input("Which option would you like to choose:\n1.Open Account\n2.Select Account\n3.Exit\n")
    return choice
  def showAccountMenu():
     choice2=input("Which option would you like to choose:\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account\n")
     return choice2

class accounts(program):
  def __init__(self,savingsbal,name,accnum,chequingbal):
   self.savingsbal=savingsbal
   self.name=name
   self.accnum=accnum
   self.chequingbal=chequingbal
  def getAccountNumber():
   accNumber=input("What is your account number?\n")
   return accNumber
  def getAccountHolderName(self):
   accHolderName=input("What is your Name\n")
  # def getRateOfInterest():
  # =input("")
  def getCurrentBalance(self):
   bal=input("")
  #  deposit=input("")
  #  withdraw=input("")
  def deposit(accbal):
    accbal+=int(input("How much would you like to deposit\n"))
    print("Youre new balance is", accbal)
    return accbal
  def widthdraw(accbal):
    widthdrawamount=int(input("How much would you like to widthdraw\n"))
    while accbal-widthdrawamount<=5000:
     print("Your savings account requires a minimum balance of $5000\nIf you would like to cancel the widthdraw, type 'exit', otherwise,please try again")
     widthdrawamount=(input("How much would you like to widthdraw\n"))
     if widthdrawamount=='exit':
      break
     else:
      widthdrawamount=int(widthdrawamount)
    else:
     accbal-=widthdrawamount
    print("Your balance is", accbal)
    return accbal
    


# class showAccountMenu:
#     def checkbal():
#     def deposit():
#     def withdraw():
#     def exitacc():



match program.showMainMenu():
 case '1':
    input('')
 case '2':
   accdetails= accounts.getAccountNumber()
   match accdetails:
    case '1':
     x=accounts(10000,'Jordan',1,10000)
    case '2':
     y=accounts(20000,'Sylvester',3,15000)
    case '3':
     z=accounts(30000,'Mark',3,20000)
   match program.showAccountMenu():
    case '1':
      if accdetails=='1':
       print("Ypur chequing balance is:",x.chequingbal,"\nYour savings balance is:" ,x.savingsbal)
      if accdetails=='2':
       print("Ypur chequing balance is:",y.chequingbal,"\nYour savings balance is:" ,y.savingsbal)
      if accdetails=='3':
       print("Ypur chequing balance is:",z.chequingbal,"\nYour savings balance is:" ,z.savingsbal)
    case '2':
      if accdetails=='1':
       x.savingsbal=accounts.deposit(x.savingsbal)
      if accdetails=='2':
       y.savingsbal=accounts.deposit(y.savingsbal)
      if accdetails=='3':
       z.savingsbal=accounts.deposit(z.savingsbal)
    case'3':
     if accdetails=='1':
       x.savingsbal=accounts.widthdraw(x.savingsbal)
     if accdetails=='2':
       y.savingsbal=accounts.widthdraw(y.savingsbal)
     if accdetails=='3':
       z.savingsbal=accounts.widthdraw(z.savingsbal)   
 case '3':
    exit()

  




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