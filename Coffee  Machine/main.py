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
}


def check_resources(order):
    """checks user's selection against the amount of resources left and returns whether the drink can be made or not"""
    if order == "espresso":
        order_water = MENU[order]["ingredients"]["water"]
        order_coffee = MENU[order]["ingredients"]["coffee"]
        if order_water > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif order_coffee > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    else:
        order_water = MENU[order]["ingredients"]["water"]
        order_milk = MENU[order]["ingredients"]["milk"]
        order_coffee = MENU[order]["ingredients"]["coffee"]
        if order_water > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif order_milk > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif order_coffee > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True


def coin_processor():
    """User inserts coins and returns total amount entered."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * .25
    dimes = int(input("How many dimes? ")) * .1
    nickels = int(input("How many nickels? ")) * .05
    pennies = int(input("How many pennies? ")) * .01
    return quarters + dimes + nickels + pennies


def coin_compare(total_input, order):
    """Compares the inserted coins to the cost of the drink and returns whether there is enough or not."""
    if total_input < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def change_maker(total_input, order):
    """Gives change to user."""
    money_refunded = total_input - MENU[order]["cost"]
    money_refunded = round(money_refunded, 2)
    if money_refunded > 0:
        print(f"Here is ${money_refunded} in change.")
        return
    else:
        return


def deplete_resources(order, resources):
    """Depletes resources from total amount."""
    if order == "espresso":
        order_water = MENU[order]["ingredients"]["water"]
        order_coffee = MENU[order]["ingredients"]["coffee"]
        resources["water"] -= order_water
        resources["coffee"] -= order_coffee
        return resources
    else:
        order_water = MENU[order]["ingredients"]["water"]
        order_milk = MENU[order]["ingredients"]["milk"]
        order_coffee = MENU[order]["ingredients"]["coffee"]
        resources["water"] -= order_water
        resources["milk"] -= order_milk
        resources["coffee"] -= order_coffee
        return resources


def coffee_machine(resources):
    """Runs the coffee machine."""
    money = 0
    while True:
        order = input("What would you like? (espresso/latte/cappuccino) ").lower()
        if order == "off":
            quit()
        elif order == "report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}")
            print(f"Profit: ${money}")
        else:
            can_make_drink = check_resources(order)
            if can_make_drink:
                total_input = coin_processor()
                enough_money = coin_compare(total_input, order)
                if enough_money:
                    change_maker(total_input, order)
                    money += MENU[order]["cost"]
                    resources = deplete_resources(order, resources)
                    print(f"Here is your {order}. ☕ Enjoy!")


coffee_machine(resources)
