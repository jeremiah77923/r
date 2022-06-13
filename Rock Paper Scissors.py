import random

move = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moves = [rock, paper, scissors]
userMove = moves[move]
computerMove = random.randint(0, 2)
print("You chose:")
print(userMove)
print("The computer chose:")
print(moves[computerMove])
# Rock and Paper:
if move == 0 and computerMove == 1:
    print("The computer won")
elif move == 1 and computerMove == 0:
    print("You won")
# Paper and Scissors
elif move == 1 and computerMove == 2:
    print("The computer won")
elif move == 2 and computerMove == 1:
    print("You won")
# Rock and Scissors
elif move == 0 and computerMove == 2:
    print("You won")
elif move == 2 and computerMove == 0:
    print("The computer won")
else:
    print("It is a tie")
