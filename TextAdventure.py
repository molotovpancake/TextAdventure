def main():
  import random
  import time
  from time import sleep
  from random import randint
  
  print ("Hi")
  name = input ("What's your username? ")
  print ("OK. Hello, " + name)
  sleep (0.5)
  print ("Chapter one...")
  sleep (0.3)
  print ("You are in your house. Where do you go?")
  sleep (0.4)
  optionsloop = True
  while optionsloop == True:
    ui1 = input ("Type 'options' to see the options. ")
    if ui1 == ("options"):
      print ("Upstairs\nKitchen\nLounge\nOutside")
      optionsloop = False
    else: 
      print ("That isn't a valid answer.")
  choiceloop = True
  while choiceloop == True:
    ui1 = input ("Now choose where you want to go. ")
    if ui1 == ("Upstairs"):
      print ("There is an extremely child-proof gate blocking your way.\nIt is so child-proof that you cannot go through it. Try again at a later date.")
    elif ui1 == ("Kitchen"):
      print ("The door is very heavy. Try again later. ")
    elif ui1 == ("Lounge"):
      print ("You are now in the lounge.")
      choiceloop = False
    elif ui1 == ("Outside"):
      print ("The front door is locked.")
    else:
      print ("That is not a valid answer")

#  end = False  
#  while end == False:
  
  
main()
