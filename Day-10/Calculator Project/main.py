from contextlib import nullcontext

import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary = {
    "+": add, "-": subtract, "*": multiply, "/": divide,
}

calcContinue = True
container = [nullcontext]
while calcContinue:
    if container[0] == nullcontext:
        n1 = int(input("what is the first number: "))
    else:
        n1 = container[0]
    for operation in dictionary:
        print(operation)
    op = input("pick an operation: ")
    n2 = int(input("what is the next number: "))
    if op in dictionary:
        print(f"{n1} {op} {n2} = {dictionary[op](n1, n2)}")
    else:
        print("invalid operator")
        break

    agree = input(f"type y to continue calculating with {dictionary[op](n1, n2)},"
                  f" or type 'n' to start a new calculation: ")
    if agree == "n":
        print("\n" * 20)
        container[0] = nullcontext
    else:
        container[0] = dictionary[op](n1, n2)

