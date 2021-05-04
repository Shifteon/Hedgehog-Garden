"""
Player class. Describes the player of the game.
Author: Benjamin Wyatt
"""

from hedgehog import Hedgehog, SpecialHog
from food import Food, Orange, Cake, Kibble

class Player:
    def __init__(self, name):
        self.name = name
        # hedgehog = Hedgehog()
        self.hedgehogs = []
        # food = Kibble()
        self.food = []
        self.money = 100

    def update(self):
        if self.money < 0:
            self.money = 0

    def initializeFood(self, numKibble, numCake, numOrange):
        for i in range(numKibble):
            kibble = Kibble()
            self.food.append(kibble)
        for i in range(numCake):
            cake = Cake()
            self.food.append(cake)
        for i in range(numOrange):
            orange = Orange()
            self.food.append(orange)

    def initializeHedgehogs(self, name, hunger, health, hygiene, canGetNewHog, isSpecial):
        print(isSpecial)
        if isSpecial == False:
            hedgehog = Hedgehog()
            hedgehog.name = name
            hedgehog.hunger = hunger
            hedgehog.health = health
            hedgehog.hygiene = hygiene
            hedgehog.canGetNewHog = canGetNewHog
            self.hedgehogs.append(hedgehog)
        else:
            hedgehog = SpecialHog()
            hedgehog.name = name
            hedgehog.hunger = hunger
            hedgehog.health = health
            hedgehog.hygiene = hygiene
            hedgehog.canGetNewHog = canGetNewHog
            self.hedgehogs.append(hedgehog)