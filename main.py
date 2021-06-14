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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins ():
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many coins?: ")) * 0.25
    total += int(input("how many notes?: ")) * 100
    return total


def is_transsaction_successful(money_recieved, drink_cost):
    """Return True whrn the payments are accepted, or False if money is insufficent."""
    if money_recieved >=  drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is Rs.{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deductt the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")




is_on = True

while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transsaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
