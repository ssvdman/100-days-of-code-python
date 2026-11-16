from art import logo
print(logo)

gameOver = False

name = input("what is your name?: ")
bid = int(input("what is your bid?: "))
dictionary = {
    name: bid,
}

while not gameOver:
    # TODO-2: Save data into dictionary {name: price}
    dictionary[name] = bid

    # TODO-3: Whether if new bids need to be added
    question = input("are there any more bidders?: ").lower()
    if question == "no":
        gameOver = True
    else:
        # TODO-1: Ask the user for input
        print("\n" * 100)
        name = input("what is your name?: ")
        bid = int(input("what is your bid?: "))

# TODO-4: Compare bids in dictionary
maximum = dictionary[name]
store = name
for key in dictionary:
    if  dictionary[key] > maximum:
        maximum = dictionary[key]
        store = key
print("\n" * 100)
print(f"the winner is {store} with a bid of ${maximum}")
