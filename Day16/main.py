
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine= MoneyMachine()
coffee_maker= CoffeeMaker()
menu= Menu()
is_on=True

items= menu.get_items()

while is_on:
    order= input(f"What would you like? ({items}) ")

    if order== 'off':
        is_on= False
    elif order=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        drinks= menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drinks):
            if money_machine.make_payment(drinks.cost):
                 coffee_maker.make_coffee(drinks)

            # is_on = False










