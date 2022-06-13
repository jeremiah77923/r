# Created by Jeremiah Hawthorne
# Finished on Monday, June 14th, 2021

user_Name = input("What is your name?\n")
print("Welcome to the Treasure Island, " + user_Name + ".")
print("Your mission is to find the treasure")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
cross_Road1 = input("You are at a crossroad. Where do you want to go? Type \"Left\" or \"Right\"\n")
if cross_Road1.lower() == "left":
    print("You have arrived at a lake but if you wish to find the treasure you must go the other side of the lake")
    cross_Road2 = input("Do you want to swim(type \"swim\") across or wait for a boat(type \"boat\")?\n")
    if cross_Road2.lower() == "boat":
        print("You made it to the other side of the lake and have arrived at a mysterious house.")
        print("There are 4 different colored doors(red,blue,yellow,black) you have to choose from, three of them "
              "lead to death, "
              "but one of them leads to the treasure")
        cross_Road3 = input("Type \"red\",\"blue\",\"yellow\",or \"black\"\n")
        if cross_Road3.lower() == "Yellow":
            print("You won the game!!")
        elif cross_Road3.lower() == "blue":
            print("You entered the blue door, but you were eaten by beasts, game over... ")
        elif cross_Road3.lower() == "black":
            print("You entered the black door, but you drowned after the room filled with water, game over...")
        elif cross_Road3.lower() == "red":
            print("You entered the red door, but you were burned by fire, game over...")
        else:
            print("You lost the game.")
    else:
        print("You were eaten by Piranhas, game over...")

else:
    print("You fell in a hole and died, game over...")

# Created by Jeremiah Hawthorne
# Finished on Monday, June 14th, 2021
