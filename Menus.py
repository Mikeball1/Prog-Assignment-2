class program:
  def showMainMenu():
    choice=input("Which option would you like to choose:\n1.Open Account\n2.Select Account\n3.Exit\n")
    while choice!='1' and choice!='2' and choice!='3':
     print("Please input one of the given options")
     choice=input("Which option would you like to choose:\n1.Open Account\n2.Select Account\n3.Exit\n")
    return choice
#Provides user with account menu choice when called
  def showAccountMenu():
     choice2=input("Which option would you like to choose:\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account\n")
     while choice2!='1' and choice2!='2' and choice2!='3' and choice2!='4':
        choice2=input("Which option would you like to choose:\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account\n")
     return choice2