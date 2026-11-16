import art
import random

def keep_going():
    agree = input("do you want to play a game of blackjack? type 'y' or 'n': ")
    if agree == "n":
        return False
    else:
        return True

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
myCard = []
compCard = []

def show_score():
    print("\n")
    print(f"your final hand: {myCard}, final score: {myScore}")
    print(f"computer's final hand: {compCard}, final score: {compScore}")

while keep_going():
    print("\n" * 20)
    print(art.logo)

    myScore = 0
    compScore = 0
    for i in range(0, 2):
        myCard.append(random.choice(cards))
        myScore += myCard[i]
        compCard.append(random.choice(cards))
        compScore += compCard[i]

    print(f"your cards: {myCard}, current score: {myScore}")
    print(f"computer's first card: {compCard[0]}")

    def card_add(give_list, give_score):
        new_card = random.choice(cards)
        # ace (11) can be either 11 or 1
        if new_card == 11 and give_score >= 11:
            new_card = 1
        give_list.append(new_card)
        give_score += new_card
        return give_score

    while myScore <= 21:
        takeCard = input("type 'y' to get another card, type 'n' to pass: ")
        #if yes go into loop
        if takeCard == "y":
            myScore = card_add(myCard, myScore)
            print(f"your cards: {myCard}, current score: {myScore}")
            print(f"computer's first card: {compCard[0]}")

            # check if computer needs to increase now
            choices = ["y", "n"]
            compChoice = random.choice(choices)
            if compScore <= 16:
                compChoice = "y"
            if compChoice == "y":
                #call function
                compScore = card_add(compCard, compScore)

        # if user says no, then end game
        else:
            break

    if myScore > 21:
        show_score()
        print("you lose, went overboard")
        break
    elif compScore > 21:
        show_score()
        print("you win, comp went overboard")
        break
    elif myScore == compScore:
        show_score()
        print("draw")
    else:
        show_score()
        if compScore > myScore:
            print("you lose")
        else:
            print("you win")
