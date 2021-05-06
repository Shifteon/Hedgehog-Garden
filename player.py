"""
Player class. Describes the player of the game.
Author: Benjamin Wyatt
"""

from hedgehog import Hedgehog, SpecialHog
from food import Orange, Cake, Kibble

class Player:
    def __init__(self, name):
        self.name = name
        self.hedgehogs = []
        self.food = []
        self.money = 100

    def update(self):
        """
        Things that need to happen every loop iteration.
        """
        # Make sure the player's money doesn't go below 0
        if self.money < 0:
            self.money = 0

    def initializeFood(self, numKibble, numCake, numOrange):
        """
        Run at load. Add food to player
        """

        # Add food to player
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
        """
        Run at load. Add hedgehogs to user
        """
        # Is it a special hedgehog or a normal one?
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