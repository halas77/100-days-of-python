from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

while is_on:
    total_money = 0
    maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        maker.report()
        money_machine.report()
    else:
        if maker.is_resource_sufficient(menu.get_items):
            price = money_machine.process_coins
            if money_machine.make_payment(price):
                total_money += price 
                
                
                
            




