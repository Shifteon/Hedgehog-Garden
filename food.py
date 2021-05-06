"""
All of the games food.
Author: Benjamin Wyatt
"""

class Food:
    def __init__(self):
        self.calories = 100
        self.nourishment = 50

class Orange(Food):
    def __init__(self):
        self.calories = 100
        self.nourishment = 20
        self.name = "Orange"
        self.price = 150

class Cake(Food):
    def __init__(self):
        super().__init__()
        self.calories = 200
        self.nourishment = -10
        self.name = "Cake"
        self.price = 100

class Kibble(Food):
    def __init__(self):
        super().__init__()
        self.calories = 50
        self.nourishment = 0
        self.name = "Kibble"
        self.price = 50