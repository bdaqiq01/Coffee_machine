"""
Coffee Machine Class

This script defines a CoffeeMachine class that simulates a simple coffee vending machine.
The class can optionally be initialized with specified amounts of water, coffee, and milk.
 It includes the following key features:

1. Ingredient Check: Ensures there are enough ingredients (water, coffee, and milk) to make a cup of coffee.
2. Make Coffee: Prompts the user to insert dollar bills and change.
 If sufficient funds are provided, it makes a cup of coffee, deducts the used ingredients, and returns any excess change.
  If funds are insufficient, it notifies the user.
3. if the user enters coffee close, or if it doesnt want another coffee the machine closes.
"""



class CoffeeMachine:
    def __init__(self, milk= 30, coffee=30, water=30):
        # milk, coffee and water initialized amounts
        self.milk = milk
        self.coffee = coffee
        self.water = water

    def pay(self):
        global coffee_price
        quarters = float(input('Please enter number of one dollar bill '))
        dimes = float(input('Please enter your change '))
        total = quarters + (dimes / 100)
        print(f"Total: {round(total, 2)}")
        if total - coffee_price < 0:
            print(' Sorry not enough funds')
            return False
        else:
            print(f' change: {total - coffee_price}')
            return True

    def make_coffee(self):  # function
        milk_used = 5
        water_used = 10
        coffee_used = 10

        try:
            assert self.milk - milk_used >= 0, 'Not enough milk'
            assert self.water - water_used >= 0, 'Not enough water'
            assert self.coffee - coffee_used >= 0, 'Not enough coffee'
            self.milk -= milk_used
            self.coffee -= coffee_used
            self.water -= water_used
            if self.pay():
                print('Here is your coffee, Enjoy')
        except AssertionError as e:
            print(e.args[0])

    def machine_status(self):
        return f'milk: {self.milk}, water: {self.water}, coffee: {self.coffee}'


coffee_price = 2.5
myCoffeeMachine = CoffeeMachine()

coffee_shop = 'open'

while coffee_shop == 'open':
    myCoffeeMachine.make_coffee()
    another_order = input('Would you like a coffee? ')
    if another_order == 'close' or another_order == 'no':
        coffee_shop = 'close'

