from Bank_Account import *
from Menus import *
from Bank import *
from Input_Tests import *
#Present the intial welcome to the end user
def run():
 print("Welcome To Supreme Bank\nPress Any Key To Continue")
 input("")
run()
#Used for widthdraw and deposit amount
class accounts(bank):
#Requests account number
  def searchaccount():
   accNumber=notfloat("What is your account number?\n")
   return accNumber
  #Requests users deposit amount and adds to current account balance depending on the account chosen
  def deposit(accbal):
    accbal+=rightinput("How much would you like to deposit\n")
    print("Youre new balance deposit balance is", accbal)
    return accbal
  #Requests users widtdraw amount and subtracts to current account balance depending on the account chosen
  def widthdraw(accbal):
   if acchoice=='1':
    widthdrawamount=(rightinput("How much would you like to widthdraw\n"))
#Ensures savings balance is never less than $5000
    while int(accbal)-widthdrawamount<=5000:
     print("Your savings account requires a minimum balance of $5000\nIf you would like to cancel the widthdraw, type '0', otherwise,please try again")
     widthdrawamount=(rightinput("How much would you like to widthdraw\n"))
    else:
     accbal-=widthdrawamount
     print("Your savings balance is $", accbal)
     return int(accbal)
#Ensures widthraw amount is no more than $5000 over chequing balance
   if acchoice=="2":
    widthdrawamount=rightinput("How much would you like to widthdraw\n")
    while widthdrawamount>accbal+5000:
      widthdrawamount= rightinput("You may widthdraw up to $5000 over your current chequing balance\nIf you would like to cancel the widthdraw, type '0', otherwise,please try again\n")
    else:
     accbal-=widthdrawamount
    print("Your chequing balance is $", accbal)
    return int(accbal)

#Runs the program until users decides to exit
while True:
 match program.showMainMenu():

  case '1':
    print("Open account still under construction, please try again later")
  case '2':
  #Assigns bank account info based on user input
   bankacc= int((accounts.searchaccount()))
  #Checks to see if bank account exists, if account does not exist, it requests reinput
   while bankacc>len(banklist)-1:
    print("This account does not exist within our system please try again")
    bankacc= int((accounts.searchaccount()))
   accdetails=banklist[bankacc]
   m=accounts(accdetails[0],accdetails[1],accdetails[2],accdetails[3])
   while True:
    #Requests users input on what they would like to do with their account
    match program.showAccountMenu():
     case '1':
      #Displays account information
       print("Your chequing balance is:",m.savingsbal,"\nYour savings balance is:" ,m.chequingbal,"\nYour total balance is:",m.savingsbal+m.chequingbal)
     case '2':
      #Allows user to deposit depending on which account they would like to use
      acchoice=input("Would you like to deposit to your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      #Checks if user has input one of the options, if not, sends request again
      while acchoice!= '1' and acchoice!='2':
        print("Please input one of the given options")
        acchoice=input("Would you like to deposit to your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      if acchoice=='1':
         m.savingsbal=accounts.deposit(m.savingsbal)
      if acchoice=='2':
         m.chequingbal=accounts.deposit(m.chequingbal)

     case'3':
      #Allows user to widthdraw depending on which account they would like to use
      acchoice=input("Would you like to widthdraw your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      #Checks if user has input one of the options, if not, sends request again
      while acchoice!= '1' and acchoice!='2':
       print("Please input one of the given options")
       acchoice=input("Would you like to widthdraw your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      if acchoice=='1':
         m.savingsbal=accounts.widthdraw(m.savingsbal)
      if acchoice=='2':
         m.chequingbal=accounts.widthdraw(m.chequingbal)

     case '4':
      #Sets all the change to the accounts permanantly until the program is exited, this means user can enter mulitiple accounts, 
      #change information and once they return the information will remain changed for the duration of the program
      accdetails=list(accdetails)
      accdetails[0]=m.savingsbal
      accdetails[3]=m.chequingbal
      accdetails=tuple(accdetails)
      banklist[bankacc]=(accdetails[0],accdetails[1],accdetails[2],accdetails[3])

      break
#Exits program
  case '3':
   exit()

