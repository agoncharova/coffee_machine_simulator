from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


continue_customer = True
coffee_maker = CoffeeMaker()
mm = Menu()
money_machine = MoneyMachine()
while continue_customer:
    order_name = input(f"What would you like? ({Menu().get_items()})")
    drink = mm.find_drink(order_name)
    if order_name == 'off':
        continue_customer = False
    elif order_name == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order_name == 'espresso' or order_name == 'latte' or order_name == 'cappuccino':
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
             coffee_maker.make_coffee(drink)





