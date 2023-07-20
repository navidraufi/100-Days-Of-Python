from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

available_menu = Menu()
coffeeMaker = CoffeeMaker()
money_calculate = MoneyMachine()

is_on = True

while is_on:
    user_choice = input("What would you like to have?" + available_menu.get_items() + "\n").lower()

    if user_choice == "report":
        coffeeMaker.report()
        money_calculate.report()
    else:
        coffee_type = available_menu.find_drink(user_choice)
        if coffeeMaker.is_resource_sufficient(coffee_type):
            if money_calculate.make_payment(coffee_type.cost):
                coffeeMaker.make_coffee(coffee_type)

