"""
This programs
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


#TODO: make it too keep asking until it is off

coffee_price = 2.5
myCoffeeMachine = CoffeeMachine()

coffee_shop = 'open'

while coffee_shop == 'open':
    myCoffeeMachine.make_coffee()
    another_order = input('Would you like a coffee? ')
    if another_order == 'close' or another_order == 'no':
        coffee_shop = 'close'



#assert myCoffeeMachine.make_coffee() == 'Here is your coffee, Enjoy', 'could not make your coffee, sorry'
#assert myCoffeeMachine.make_coffee() == 'Not enough water', 'ingredient problems'
#assert myCoffeeMachine.machine_status() == 'milk: 5, water: 0, coffee: 0', 'status problem'
