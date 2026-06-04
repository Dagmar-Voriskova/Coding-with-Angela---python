import random

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

options = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if player >=0 and player <= 2:
    print(options[player])
    comp = random.randint(0,2)
    print(f"Computer chose:{options[comp]}")

    if player == comp:
        print("Draw!")

    elif player == 0 and comp == 1:
        print("Paper beats Rock, you lose!")
    elif player == 0 and comp == 2:
        print("Rock beats Scissors, you win!")

    elif player == 1 and comp == 2:
        print("Scissors beat Paper, you lose!")
    elif player == 1 and comp == 0:
        print("Paper beats Rock, you win!")

    elif player == 2 and comp == 0:
        print("Rock beats Scissors, you lose!")
    elif player == 2 and comp == 1:
        print("Scissors beat Paper, you win!")

else:
    print("Invalid input, try again!")
