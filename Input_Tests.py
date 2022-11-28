#Tests if input can be converted to float and request input until it does
def rightinput(test):
  while True:
   try:
    answer=float(input(test))
    if answer<=0:
      print("Please input a number greater than 0")
    else:
     return answer
   except:
    print("Please input a number")
    pass
#Tests if input can be converted to int and request input until it does
#Used when selecting menu options and account
def notfloat(test):
  while True:
   try:
    answer=int(input(test))
    if answer<=0:
      print("Please input a number greater than 0")
    else:
     return answer
   except:
    print("Please input a number")
    pass
