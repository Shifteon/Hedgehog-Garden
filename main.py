from hedgehog import Hedgehog, SpecialHog
from food import Food, Orange
from player import Player
from game import Game

hedgehog = Hedgehog()
hedgehog2 = SpecialHog()
orange = Orange()
hedgehog.draw()
hedgehog.feed(orange)
# hedgehog2.feed(orange)
# hedgehog.displayStatus()
# print(hedgehog.hunger)
hedgehog2.displayStatus()