def main():
  import random
  import time
  from time import sleep
  from random import randint
  
  print ("Hi")
  name = input ("What's your username?\n")
  print ("OK. Hello, " + name)
  sleep (0.5)
  print ("Chapter one...")
  sleep (0.3)
  print ("You are in your house. Where do you go?")
  sleep (0.4)
  optionsloop = True
  while optionsloop == True:
    ui1 = input ("Type 'options' to see the options.\n")
    if ui1 == ("options"):
      print ("Upstairs\nKitchen\nLounge\nOutside")
      optionsloop = False
    else: 
      print ("That isn't a valid answer.")
  choiceloop = True
  while choiceloop == True:
    ui1 = input ("Now choose where you want to go.\n")
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
  inv = []
  searchloop = True
  while searchloop == True:
    print ("You need to eat something. You will want to search this room.")
    sleep(0.1)
    ui1 = input ("Type Search to search somewhere in this room.\n")
    if ui1 == ("Search"):
      ui1 = input ("Search what? The options are: \ncoffee table\ndrawers\nbookshelf\nsofa\n")
      if ui1 == ("coffee table"):
        print ("You found an apple! This will be added to your inventory. Type 'inv' at any time to view your inventory. ")
        inv.insert(0,"apple")
        print (inv)
        searchloop = False
      elif ui1 == ("sofa"):
        print ("There is actually a million dollars inside this sofa. Shame they're useless. ")
      elif ui1 == ("bookshelf"):
        print ("Ugh, just a bunch of books. None of them are any use.")
      elif ui1 == ("drawers"):
        print ("Hmm... Wires, cables, a keyboard... nothing of any use to you.")
      else:
        print ("That is an invalid answer. ")
    else:
      print ("That is not a valid answer. ")
  
#  end = False  
#  while end == False:
    
  
  
main()
