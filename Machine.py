from Menu import Menu, MenuItem

from money_machine import MoneyMachine
import repl
coffee = CoffeeMaker()
coffee_menu = Menu()
money = MoneyMachine()
user_name = input("What is your name?\n")
print(f"Welcome to the coffee machine, {user_name}!!")
while True:
    user_type = input("If you are a customer(type \"c\") if you are a maintainer of the coffee machine type \"m\".\n")
    if user_type == "c":
        print(coffee_menu.get_items())
        choice = input("What would you like to drink? Type \"e\" for an espresso, type \"c\" for cappuccino, "
                       "or type \"l\" for a latte.\n")
        choice_obj = coffee_menu.menu[coffee_menu.set_choice(choice=choice)]
        if coffee.is_resource_sufficient(coffee_menu.set_ingridents(choice=choice)):
            print(f"Please enter ${choice_obj.cost} in coins below.\n")
        elif coffee.is_resource_sufficient(coffee_menu.set_ingridents(choice=choice)) == False:
            print("Tell the maintainer of the machine to put in more ingredients.")
            break
        if money.make_payment(choice_obj.cost):
            print(f"You {choice_obj.name} is being made.")
            coffee.make_coffee(coffee_menu.set_ingridents(choice))
            print(f"Here is ☕️ {choice_obj.name} {user_name} enjoy!!!\n")
    elif user_type == "m":
        choice = input("Type \"t\" to turn off the machine, or type \"r\" to get a report of the current resources in "
                       "the machine.\n").lower()
        if choice == "r":
            coffee.report()
            money.report()
        elif choice == "t":
            print("The machine has been turned off.")
            break