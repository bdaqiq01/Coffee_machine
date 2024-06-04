"""
This programs
"""

class CoffeeMachine:
    
    def __init__(self, milk = 10 , coffee = 10, water = 10):
        # milk, coffee and water initialized amounts
        self.milk = milk
        self.coffee = coffee
        self.water = water

    def make_coffee(self): # function
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

        return 'Here is your coffee, Enjoy'
      except AssertionError as e:
        return e.args[0]

    def machine_status(self):
      return f'milk: {self.milk}, water: {self.water}, coffee: {self.coffee}'


myCoffeeMachine = CoffeeMachine()
assert myCoffeeMachine.make_coffee() == 'Here is your coffee, Enjoy', 'could not make your coffee, sorry'
assert myCoffeeMachine.make_coffee() == 'Not enough water', 'ingredient problems'
assert myCoffeeMachine.machine_status() == 'milk: 5, water: 0, coffee: 0', 'status problem'