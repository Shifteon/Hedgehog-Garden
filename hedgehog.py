from food import Food, Orange

class Hedgehog:
    def __init__(self):
        self.name = "Harry"
        self.hunger = 500
        self.health = 100
        self.hygeine = 100
        self.canGetNewHog = True
        # Max stats for hedgehog. Hunger, health, hygeine
        self.maxStats = (0, 500, 500)

    def feed(self, Food):
        if (self.hunger > 0):
            self.hunger -= Food.calories
        if (self.hunger < 0):
            self.hunger = 0
        self.health += Food.nourishment
        if (self.health < 0):
            self.health = 0
        if (self.health > 500):
            self.health = 500
        if (Food.hasEffect):
            Food.applyEffect()

    def wash(self):
        if (self.hygeine < 500):
            self.hygeine += 20
        if (self.hygeine > 500):
            self.hygeine = 500

    def exercise(self):
        if (self.health < 500):
            self.health += 20
        if (self.health > 500):
            self.health = 500
        if (self.hygeine > 0):
            self.hygeine -= 10

    def draw(self):
        print(self.name)
        print(" .|||||||||. \n|||||||||||||\n|||||||||||' .\\\n`||||||||||_,__o")

    def displayStatus(self):
        print("Health: ", self.health)
        print("Hunger: ", self.hunger)
        print("Hygeine:", self.hygeine)
        
    def isMaxStatus(self):
        return self.hunger == self.maxStats[0] and self.health == self.maxStats[1] and self.hygeine == self.maxStats[2]

class SpecialHog(Hedgehog):
    def __init__(self):
        super().__init__()
        self.hunger = 2000
        self.maxStats = (0, 2000, 2000)
        self.canGetNewHog = False
    
    def draw(self):
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
