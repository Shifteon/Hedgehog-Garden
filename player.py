from hedgehog import Hedgehog

class Player:
    def __init__(self, name):
        self.name = name
        hedgehog = Hedgehog()
        self.hedgehogs = [hedgehog]
        self.food = []
        self.money = 100