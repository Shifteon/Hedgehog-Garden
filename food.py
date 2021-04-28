class Food:
    def __init__(self):
        self.calories = 100
        self.nourishment = 50
        self.hasEffect = False

class Orange(Food):
    def __init__(self):
        self.calories = 100
        self.nourishment = 20
        self.hasEffect = True
    def applyEffect(self):
        pass

class Cake(Food):
    def __init__(self):
        super().__init__()
        self.calories = 200
        self.nourishment = -10

class Kibble(Food):
    def __init__(self):
        super().__init__()
        self.calories = 50
        self.nourishment = 0