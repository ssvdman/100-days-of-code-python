MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def prompt_user():
    ask = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return ask

def print_resources():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk:  {resources["milk"]}ml")
    print(f"coffee:  {resources["coffee"]}ml")
    print(f"Money: ${resources["money"]}")

def check_sufficient(drink):
    if drink in MENU:
        for key in resources:
            if key not in MENU[drink]["ingredients"]:
                continue
            elif resources[key] < MENU[drink]["ingredients"][key]:
                return key
        return True
    else:
        print("invalid drink")
        return -1

def process_coins(choice):
    coin_needed = MENU[choice]["cost"]
    print(f"insert ${coin_needed}")

    quarter = float(input("Enter quarters: ")) * 0.25
    dimes = float(input("Enter dimes: ")) * 0.10
    nickel = float(input("Enter nickels: ")) * 0.05
    pennies = float(input("Enter pennies: ")) * 0.01

    total = quarter + dimes + nickel + pennies
    return total

def check_validity(choice):
    coin_needed = MENU[choice]["cost"]
    money = process_coins(choice)
    if money < coin_needed:
        return False
    else:
        change = money - coin_needed
        rounded_change = round(change, 2)
        resources["money"] += coin_needed
        if rounded_change > 0:
            print(f"Here is ${rounded_change} dollars in change")
            return True
        print("Transaction complete")
        return True

def deplete_resource(choice):
    if choice in MENU:
        for key in resources:
            if key not in MENU[choice]["ingredients"]:
                continue
            else:
                resources[key] -= MENU[choice]["ingredients"][key]
        return True
    else:
        print("invalid drink")
        return -2

machineOn = True
while machineOn:
# TODO 1: prompt the user
    prompt = prompt_user()

# TODO 2: turn off machine feature
    if prompt == "off":
        machineOn = False
        print("Machine turned off")

# TODO 3: report function
    elif prompt == "report":
        print_resources()

# TODO 4: check resources sufficient?
    else:
        feedback = check_sufficient(prompt)
        if not feedback == True:
            print(f"Sorry there is not enough {feedback}")
        else:
# TODO 5: if sufficient resources then request user for coins
# made a function for TODO 5
# TODO 6: transaction successful?
            if check_validity(prompt) == True:
                deplete_resource(prompt)
                print(f"Here is your {prompt}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")