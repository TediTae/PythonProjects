from art import logo

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

def check_resources(order_ingredients):
    """Returns true when resources are sufficient and false otherwise."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            needed_resource_amount = order_ingredients[item] - resources[item]
            print(f"Sorry not enough {item} for your {choice}.")
            print(f"You need to put {needed_resource_amount}ml. {item}.")
            return False
    return  True

def total_coin_calculation():
    """Returns the total calculated from the coins inserted."""
    print("Please insert a coin.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_payment_enough(payment_received, cost_of_coffee):
    """Checks the price of the coffee and payment.
     If payments is enough for coffee price returns True otherwise returns False"""
    if payment_received >= cost_of_coffee:
        change = round(payment_received - cost_of_coffee, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += cost_of_coffee
        return  True
    else:
        needed_amount = round(cost_of_coffee - payment_received, 2)
        print("Sorry that's not enough money. Money refunded.")
        print(f"You need to insert: ${needed_amount}.")
        return False

def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name}")



profit = 0
keep_working = True

while keep_working:
    print(logo)
    choice = input("What would you like to drink today? (espresso/latte/cappuccino): ")
    if choice == "off":
        keep_working = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = total_coin_calculation()
            if is_payment_enough(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


