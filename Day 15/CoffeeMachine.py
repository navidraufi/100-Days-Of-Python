def calculate_money():
    dime = int(input("How many Dimes? "))
    nickel = int(input("How many Nickels? "))
    penny = int(input("How many Penny? "))
    quarter = int(input("How many Quarter? "))

    user_money = (dime * 0.1) + (nickel * 0.05) + (penny * 0.01) + (quarter * 0.25)

    return user_money


coffee_prices = {
        "latte": {
            "water": 100,
            "milk": 50,
            "coffee": 18,
            "price": 1.5
        },
        "espresso": {
            "water": 75,
            "milk": 100,
            "coffee": 24,
            "price": 2.5
        },
        "cappuccino": {
            "water": 50,
            "milk": 125,
            "coffee": 24,
            "price": 3
        }
    }


def calculate(coffee_type, resources):

    total_price = 0
    user_money = 0

    coffee_name = ""
    coffees = ["espresso", "latte", "cappuccino"]

    if coffee_type == "huhuhuasas2":
        print("Invalid input!")
    else:
        if coffee_type == "espresso":
            resources["water"] -= coffee_prices["espresso"]["water"]
            resources["milk"] -= coffee_prices["espresso"]["milk"]
            resources["coffee"] -= coffee_prices["espresso"]["coffee"]
            coffee_name = "Espresso"

            total_price = coffee_prices["espresso"]["price"]

        elif coffee_type == "latte":
            resources["water"] -= coffee_prices["latte"]["water"]
            resources["milk"] -= coffee_prices["latte"]["milk"]
            resources["coffee"] -= coffee_prices["latte"]["coffee"]
            coffee_name = "Latte"

            total_price = coffee_prices["latte"]["price"]

        elif coffee_type == "cappuccino":

            resources["water"] -= coffee_prices["cappuccino"]["water"]
            resources["milk"] -= coffee_prices["cappuccino"]["milk"]
            resources["coffee"] -= coffee_prices["cappuccino"]["coffee"]

            coffee_name = "Cappuccino"

            total_price = coffee_prices["cappuccino"]["price"]
        else:
            print("Wrong input!")
        if coffee_type in coffees:
            user_money = calculate_money()
            if total_price > user_money:
                print(f"You have insufficient money, you need ${total_price - user_money} to buy a {coffee_name}. ")
            else:
                if user_money - total_price == 0:
                    print(f"Here is your {coffee_name} enjoy.")
                else:
                    print(f"Here is your {coffee_name} enjoy.\nAnd here is your ${round((user_money - total_price),2)} change.")


stop = False

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def calculate_resource(materials,type_of_coffee):
    if materials["water"] < coffee_prices[type_of_coffee]["water"] or materials["milk"] < coffee_prices[type_of_coffee]["milk"] or materials["coffee"] < coffee_prices[type_of_coffee]["coffee"]:
        return True
    else:
        return False


valid_choices = ["cappuccino", "espresso", "latte", "restore", "exit", "report"]

while not stop:

    user_choice = input(
        "What kind of coffee would you like? 'Cappuccino', 'Espresso' or 'Latte' (only letter is enough) \n").lower()
    if user_choice in valid_choices:

        if user_choice == "exit":
            stop = True
            break

        if user_choice == "restore":
            resource["water"] = 300
            resource["milk"] = 200
            resource["coffee"] = 100
        elif user_choice == "report":
            print(f"You have {resource['water']}ml water left.")
            print(f"You have {resource['milk']}ml milk left.")
            print(f"You have {resource['coffee']}g coffee left.")

        elif calculate_resource(resource,user_choice):
            print(f"Insufficient resources!")

        else:
            calculate(user_choice, resource)
    else:
        print("Invalid input!")