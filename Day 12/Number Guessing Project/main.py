import random
from art import logo
print(logo)

print("welcome to the number guessing game!")
print("i'm thinking of a number between 1 and 100")
chosenValue = random.randint(1, 100)
#print(f"pssst, the correct answer is {chosenValue}")

difficulty = input("choose a difficulty. type 'easy' or 'hard: ").lower()
health = 0
if difficulty == "easy":
    health = 10
    print("you have 10 attempts remaining to guess the number")
else:
    health = 5
    print("you have 5 attempts remaining to guess the number")

while health > 0:
    guess = int(input("make a guess: "))
    if guess > chosenValue:
        print("too high")
        health -= 1
    elif guess < chosenValue:
        print("too low")
        health -= 1
    else:
        print("you win! you guessed the correct number!")
        break

if health == 0:
    print(f"you lose!!, the correct number was {chosenValue}")