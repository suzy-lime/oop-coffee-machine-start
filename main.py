from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeecart_menu = Menu()

# coffeecart_items = MenuItem()

coffeecart_drink_machine = CoffeeMaker()

coffeecart_money_machine = MoneyMachine()

is_on = True

while is_on:
    options = coffeecart_menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeecart_drink_machine.report()
        coffeecart_money_machine.report()
    else:
        drink = coffeecart_menu.find_drink(choice)
        if coffeecart_drink_machine.is_resource_sufficient(drink) and coffeecart_money_machine.make_payment(drink.cost):
            coffeecart_drink_machine.make_coffee(drink)
