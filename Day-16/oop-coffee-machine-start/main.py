from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MenuObject = Menu()
CoffeeMakerObject = CoffeeMaker()
MoneyMachineObject = MoneyMachine()

machineOn = True
while machineOn:

    print(f"What would you like? ({MenuObject.get_items()})")
    choice = input()

    if choice == "off":
        machineOn = False
    elif choice == "report":
        CoffeeMakerObject.report()
        MoneyMachineObject.report()
    else:
        try:
            MenuItemObject = MenuObject.find_drink(choice)
            resource_sufficient = CoffeeMakerObject.is_resource_sufficient(MenuItemObject)
        except AttributeError:
            continue

        if resource_sufficient:
            cost = MenuItemObject.cost
            print(f"{choice} cost ${cost}")
            if MoneyMachineObject.make_payment(cost):
                CoffeeMakerObject.make_coffee(MenuItemObject)
