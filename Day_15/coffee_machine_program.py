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


# TODO: 1. Print report about all the resources in the coffee machine
#       2. Check if resources are sufficient?
#       3. Process Coins
#       4. Check if transaction successful?
#       5. Make Coffee

#
# def display_resources():
#     return f"Water: {available_water}ml \nMilk: {available_milk}ml \nCoffee: {available_coffee}g"


# def make_money_transaction(menu_item):
#     quarters = int(input("how many quarters?:"))
#     dimes = int(input("how many dimes?:"))
#     nickels = int(input("how many nickels?:"))
#     pennies = int(input("how many pennies?:"))
#     total_coins_value = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
#     cost = MENU[menu_item]["cost"]
#     if total_coins_value-cost >= 0:
#         print(f"Here is ${total_coins_value-cost} in change.")
#         global profit
#         profit += cost
#         make_order(menu_choice)
#     else:
#         print("Sorry that's not enough profit. Money refunded.")


# def make_order(menu_item):
#     available_water = resources["water"]-MENU[menu_item]["ingredients"]["water"]
#     available_coffee = resources["coffee"]-MENU[menu_item]["ingredients"]["coffee"]
#     available_milk = resources["milk"]-MENU[menu_item]["ingredients"]["milk"] if menu_item != "espresso" else resources["milk"]
#     print(f"Here is your {menu_item} ☕. Enjoy!")


# available_water = resources["water"]
# available_milk = resources["milk"]
# available_coffee = resources["coffee"]

    # elif menu_choice == "espresso":
    #     is_resource_available = check_resources(menu_choice)
    #     if is_resource_available:
    #         print("Please insert Coins")
    #         make_money_transaction(menu_choice)
    #     else:
    #         print("Sorry,there is not enough resources.")
    #
    # elif menu_choice == "latte":
    #     is_resource_available = check_resources(menu_choice)
    #     if is_resource_available:
    #         print("Please insert Coins")
    #         make_money_transaction(menu_choice)
    #     else:
    #         print("Sorry,there is not enough resources.")
    #
    # elif menu_choice == "cappuccino":
    #     is_resource_available = check_resources(menu_choice)
    #     if is_resource_available:
    #         print("Please insert Coins")
    #         make_money_transaction(menu_choice)
    #     else:
    #         print("Sorry,there is not enough resources.")


def check_resource_sufficient(order_ingredients):
    """Checks if the resources are enough to make a coffee"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters? :")) * 0.25
    total += int(input("how many dimes? :")) * 0.1
    total += int(input("how many nickels? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true when the payment is accepted, false when money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


profit = 0
machine_is_on = True

while machine_is_on:
    menu_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if menu_choice == "off":
        machine_is_on = False
        print("Turning machine Off")

    elif menu_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[menu_choice]
        if check_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(drink, drink['ingredients'])
