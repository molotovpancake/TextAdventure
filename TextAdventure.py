def main():
  import random
  import time
  from time import sleep
  from random import randint
  
  print ("Hi")
  name = input ("What's your name?\n")
  print ("OK. Hello, " + name)
  print ("A pen and paper may be necessary to write down given commands.")
  sleep (0.5)
  print ("Chapter one...")
  sleep (0.3)
  print ("You are in your house. Where do you go?")
  sleep (0.4)
  optionsloop = True
  while optionsloop == True:
    ui1 = input ("Type 'Options' to see the options.\n")
    if ui1 == ("Options"):
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
  foodstock = []
  searchloop = True
  while searchloop == True:
    print ("You need to eat something. You will want to search this room.")
    sleep(0.1)
    ui1 = input ("Type 'Search' to search somewhere in this room.\n")
    if ui1 == ("Search"):
      ui1 = input ("Search what? The options are: \ncoffee table\ndrawers\nbookshelf\nsofa\n")
      if ui1 == ("coffee table"):
        print ("You found an apple and some water! This will be added to your food stock. Type 'food' at any time to view your food stock. ")
        foodstock.insert(0,"apple")
        foodstock.insert(1,"water")
        
        string = foodstock[0]
        for item in foodstock[1:]:
          string = string + "\n" + item
        print (string)
        
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
  
  consumeloop = True
  while consumeloop == True:
    print ("Now you have something to eat, so eat it.")
    sleep(0.1)
    ui1 = input ("Type 'Consume' to consume something in your food stock.\n")
    if ui1 == ("Consume"):
      ui1 = input ("Consume what? The options are: " + string)
      if ui1 == ("apple"):
        print ("Apple consumed. You now have 20/20 health. Type 'hp' to view your health at any time. ")
        inv.insert(0,"apple")
        
        string = inv[0]
        for item in inv[1:]:
          string = string + "\n" + item
        print (string)
        
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
