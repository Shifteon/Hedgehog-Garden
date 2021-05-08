"""
Main file. Everything runs from here.
Author: Benjamin Wyatt
"""

from game import Game
import os

def cls():
    """
    Function to clear the console.
    """
    os.system('cls' if os.name=='nt' else 'clear')

name = input("Enter your name: ")
game = Game(name)
# Loop until the player quits the game
while game.menu():
    game.update()
    cls()