from art import logo
from art import vs
import random
import game_data
print(logo)

chosenList = []
def printCompare(letter, choice):
    print(f"compare {letter}: {choice["name"]}, a {choice["description"]}"
          f", from {choice["country"]}")

# if user is right: # print space # increase points
def compareWin(lis, letter):
    if letter == "A" and lis[0]["follower_count"] > lis[1]["follower_count"]:
        return True
    elif letter == "B" and lis[1]["follower_count"] > lis[0]["follower_count"]:
        return True
    else:
        return False

chosenPerson = random.choice(game_data.data)
chosenList.append(chosenPerson)
printCompare("A", chosenPerson)

count = 0
while True:
    print(vs)

    # prints out details of a random person2
    chosenPersonB = random.choice(game_data.data)
    chosenList.append(chosenPersonB)
    printCompare("B", chosenPersonB)

    # asks user input
    guess = input("who has more followers? type 'A' or 'B' ").upper()
    print("\n" * 8)

    if compareWin(chosenList, guess):
        count += 1
        chosenList.remove(random.choice(chosenList))
        print(f"you are right! current score {count}")
    else:
        print(f"sorry, that's wrong. final score: {count}")
        break

    # take the chosen person to next vs
    printCompare("A", chosenList[0])