'''
Create flower class with three variables str, int, float
that is name, no. of petals, and price
include constructor for initialising all and
methods for setting and getting all values
'''
class Flower:
    def __init__(self, name:str, no_of_petals:int, price:float):
        self._name = name
        self._no_of_petals = no_of_petals
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, name:str):
        self._name = name
    
    def get_no_of_petals(self):
        return self._no_of_petals

    def set_no_of_petals(self, no_of_petals:int):
        self._no_of_petals = no_of_petals

    def get_price(self):
        return self._price

    def set_price(self, price:float):
        self._price = price

if __name__ == "__main__":
    orchid = Flower('orchid', 5, 12.5)
    print('flower is {} with {} petals and cost ${} a piece.'
    .format(orchid.get_name(), orchid.get_no_of_petals(), orchid.get_price()))