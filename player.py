from hedgehog import Hedgehog
from food import Food, Orange, Cake, Kibble

class Player:
    def __init__(self, name):
        self.name = name
        hedgehog = Hedgehog()
        self.hedgehogs = [hedgehog]
        food = Kibble()
        self.food = [food]
        self.money = 100