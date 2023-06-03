MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

def report(resources):
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")

def check_available(order, recources):
    for n in MENU:
        if n == order:
            # print(MENU[n]['ingredients']['water'])
            if MENU[n]['ingredients']['water'] < resources['water'] and MENU[n]['ingredients']['milk'] < resources['milk'] and MENU[n]['ingredients']['coffee'] < resources['coffee']:
                return True
            else:
                return False


def change(order, total_amount):
    for n in MENU:
        if n == order:
            cost = MENU[n]['cost']
    if total_amount < cost:
        print("Sorry that's not enough money")
        return -1
    else:
        change = total_amount - cost
        return change


# print(MENU['espresso']['ingredients']['water'])
# water = 100
# milk = 200
# coffee = 100
# money=0
order = input("What would you like? (espresso/latte/cappuccino): ").lower()
if order == 'report':
    report(resources)
elif order == 'espresso' or order == 'latte' or order == 'cappuccino':

    if check_available(order, resources):
        print("Available")

        def insert_coin(profit,resources):
            print("Please insert coins")
            quatars = int(input("How many quatars? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            total_amount= 0.25 * quatars + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            return_amount = round(change(order, total_amount),2)
            if return_amount >= 0:
                profit += total_amount
                resources['water'] -= MENU[order]['ingredients']['water']
                resources['milk'] -= MENU[order]['ingredients']['milk']
                resources['coffee'] -= MENU[order]['ingredients']['coffee']
                print(f"Here is ${return_amount} in change")
            else:
                insert_coin(profit,resources)
        insert_coin(profit, resources)
        report(resources)
    else:
        print("Not Available")


