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

import random

# my own list
choices = ["rock", "paper", "scissors"]

#input
print("what do you choose? type 0 for rock, 1 for paper or 2 for scissors")
userChoice = int(input())
if userChoice == 0:
    print(rock)
elif userChoice == 1:
    print(paper)
else:
    print(scissors)

# computer choice
computerChoice = random.randint(0,2)
print("computer chose: ")
if computerChoice == 0:
    print(rock)
elif computerChoice == 1:
    print(paper)
else:
    print(scissors)

# output
if (userChoice < 0 or userChoice >= 3):
    print("invalid choice")
elif (userChoice == 0 and computerChoice == 0):
    print("draw")
elif (userChoice == 0 and computerChoice == 1):
    print("you lose!")
elif (userChoice == 0 and computerChoice == 2):
    print("you win!")
elif (userChoice == 1 and computerChoice == 0):
    print("you win!")
elif (userChoice == 1 and computerChoice == 1):
    print("draw")
elif (userChoice == 1 and computerChoice == 2):
    print("you lose!")
elif (userChoice == 2 and computerChoice == 0):
    print("you lose!")
elif (userChoice == 2 and computerChoice == 1):
    print("you win!")
elif (userChoice == 2 and computerChoice == 2):
    print("draw")
