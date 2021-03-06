"""
Hedgehog and special hedgehog class.
Author: Benjamin Wyatt
"""

from food import Food, Orange

class Hedgehog:
    def __init__(self):
        self.name = "Harry"
        self.hunger = 300
        self.health = 100
        self.hygiene = 100
        self.canGetNewHog = True
        # Max stats for hedgehog. Hunger, health, hygiene
        self.maxStats = (0, 300, 300)
        self.isSpecial = False

    def feed(self, Food):
        """
        Feed a hedgehog.
        """
        # Stay above 0
        if (self.hunger > 0):
            self.hunger -= Food.calories
        if (self.hunger < 0):
            self.hunger = 0
        self.health += Food.nourishment
        if (self.health < 0):
            self.health = 0
        if (self.health > self.maxStats[1]):
            self.health = self.maxStats[1]

    def wash(self):
        """
        Wash a hedgehog.
        """
        if (self.hygiene < self.maxStats[2]):
            self.hygiene += 20
        if (self.hygiene > self.maxStats[2]):
            self.hygiene = self.maxStats[2]

    def exercise(self):
        """
        Exercise a hedgehog.
        """
        if (self.health < self.maxStats[1]):
            self.health += 20
        if (self.health > self.maxStats[1]):
            self.health = self.maxStats[1]
        if (self.hygiene > 0):
            self.hygiene -= 10

    def draw(self):
        """
        Draw a hedgehog.
        """
        # print(self.name)
        print(" .|||||||||. \n|||||||||||||\n|||||||||||' .\\\n`||||||||||_,__o")

    def displayStatus(self):
        """
        Displays a hedgehog's status.
        """
        print("Health: ", self.health)
        print("Hunger: ", self.hunger)
        print("Hygiene:", self.hygiene)
        
    def isMaxStatus(self):
        """
        Returns True if the hedgehog has max status and False if it doesn't.
        """
        return self.hunger == self.maxStats[0] and self.health == self.maxStats[1] and self.hygiene == self.maxStats[2]

class SpecialHog(Hedgehog):
    def __init__(self):
        super().__init__()
        self.hunger = 1000
        self.maxStats = (0, 1000, 1000)
        self.canGetNewHog = False
        self.isSpecial = True
    
    def draw(self):
        """
        Draw the special hedgehog.
        """
        print(self.name + ": This is a SPECIAL Hedgehog!")
        print("""              \ / \/ \/ / ,
           \ /  \/ \/  \/  / ,
         \ \ \/ \/ \/ \ \/ \/ /
       .\  \/  \/ \/ \/  \/ / / /
      '  / / \/  \/ \/ \/  \/ \ \/ \\
   .'     ) \/ \/ \/ \/  \/  \/ \ / \\
  /   o    ) \/ \/ \/ \/ \/ \/ \// /
o'_ ',__ .'   ,.,.,.,.,.,.,.,'- '%
         // \\\\          // \\\\
        ''  ''         ''  ''""")
