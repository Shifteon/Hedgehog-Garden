from game import Game
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

name = input("Enter your name: ")
game = Game(name)
while(game.menu()):
    game.update()
    cls()