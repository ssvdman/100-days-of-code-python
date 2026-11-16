letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

bufferLetters = []
for i in range(0, nr_letters):
    container = random.randint(0, len(letters) - 1)
    bufferLetters.append(letters[container])
    # or could have used random.choice(list)

bufferSymbols = []
for i in range(0, nr_symbols):
    container = random.randint(0, len(symbols) - 1)
    bufferSymbols.append(symbols[container])


bufferNumbers = []
for i in range(0, nr_numbers):
    bufferNumbers.append(random.randint(0, 9))
# print(bufferLetters, bufferSymbols, bufferNumbers)

# my own original method
# combined = [bufferLetters, bufferSymbols, bufferNumbers]

# print(len(combined)) # len(combined) gives no. of rows
# print(len(combined[0])) # len(combined[0]) gives no. of col

#new method after finding function
import itertools
combined = list(itertools.chain(bufferLetters + bufferNumbers + bufferSymbols))
random.shuffle(combined)
for i in range(0, len(combined)):
        print(combined[i], end= "")