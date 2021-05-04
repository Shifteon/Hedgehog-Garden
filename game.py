"""
Game class to run all the game logic.
Author: Benjamin Wyatt
"""

from hedgehog import Hedgehog, SpecialHog
from food import Food, Orange, Kibble, Cake
from player import Player
from store import Store
from load_save import save, load

class Game:
    def __init__(self, name):
        self.player = Player(name)
        self.store = Store(self.player)
        load(self.player)
    

    def getInput(self, min, max): 
        """
        Function to recieve integer input.
        Enter a minimum value and a max value.
        """
        selection = input()
        # Input can't be invalid
        while selection == "" or int(selection) < min or int(selection) > max:
            selection = input("Please input a valid option: ")
        return int(selection)

    def displayHedgehogs(self):
        """
        Displays all the player's hedgehogs
        """
        i = 1
        for hedgehog in self.player.hedgehogs:
            print("Hedgehog number {}: {}".format(i, hedgehog.name))
            hedgehog.draw()
            i += 1

    def displayFood(self):
        """
        Displays all the player's food
        """
        if len(self.player.food) == 0:
            input("You are all out of food! Go buy some at the shop! [ENTER]")
        else:
            i = 1
            for food in self.player.food:
                print("Food number {}: {}".format(i, food.name))
                i += 1

    def feed(self):
        """
        Feed a specific hedgehog.
        """
        if len(self.player.food) == 0:
            print("Sorry! You have no food. Go buy some at the shop!")
            input("Press ENTER to continue: ")
            return
        # Select a hedgehog
        print("Select a hedgehog by number: ")
        self.displayHedgehogs()
        hedgehogNum = self.getInput(1, len(self.player.hedgehogs))

        # Select what to feed it
        print("Select a food: ")
        self.displayFood()
        foodNum = self.getInput(1, len(self.player.food))

        # Feed the hedgehog and remove the food fed from the player
        self.player.hedgehogs[hedgehogNum - 1].feed(self.player.food[foodNum - 1])
        self.player.food.pop(foodNum - 1)

        # Let the player know that their hedgehog has been fed
        print("{} has been fed!".format(self.player.hedgehogs[hedgehogNum - 1].name))
        input("Press ENTER to continue: ")

    def exercise(self):
        """
        Exercise a specific hedgehog.
        """
        # Select a hedgehog
        print("Select a hedgehog by number: ")
        self.displayHedgehogs()
        hedgehogNum = self.getInput(1, len(self.player.hedgehogs))

        # Exercise the hedgehog
        self.player.hedgehogs[hedgehogNum - 1].exercise()

        # Let the player know that their hedgehog has been exercised
        input("{} has been exercised! [ENTER]".format(self.player.hedgehogs[hedgehogNum - 1].name))
        print("You earned $25!")
        self.player.money += 25
        input("Press ENTER to continue: ")

    def wash(self):
        """
        Wash a specific hedgehog.
        """
        # Select a hedgehog
        print("Select a hedgehog by number: ")
        self.displayHedgehogs()
        hedgehogNum = self.getInput(1, len(self.player.hedgehogs))

        # Wash the hedgehog
        self.player.hedgehogs[hedgehogNum - 1].wash()

        # Let the player know that their hedgehog has been washed
        input("{} has been washed! [ENTER]".format(self.player.hedgehogs[hedgehogNum - 1].name))
        print("You earned $25!")
        self.player.money += 25
        input("Press ENTER to continue: ")


    def menu(self):
        """
        The main menu and the starting point of the game.
        """
        print("Select an Option")
        print("1 - Display Hedgehogs")
        print("2 - Display Hedgehog status")
        print("3 - Display Food")
        print("4 - Feed")
        print("5 - Wash")
        print("6 - Exercise")
        print("7 - Shop")
        print("8 - Save and Quit")

        # Get the player's selection and act on it
        selection = self.getInput(1, 9)
        if selection == 1:
            self.displayHedgehogs()
            input("Press ENTER to continue: ")
        elif selection == 2:
            self.displayStatus()
        elif selection == 3:
            self.displayFood()
            input("Press ENTER to continue: ")
        elif selection == 4:
            self.feed()
        elif selection == 5:
            self.wash()
        elif selection == 6:
            self.exercise()
        elif selection == 7:
            self.store.purchase()
            input("Press ENTER to continue: ")
        elif selection == 8:
            save(self.player)
            return False
        # For debugging. Remove for actual product
        elif selection == 9:
            newHedgehog = SpecialHog()
            self.player.hedgehogs.append(newHedgehog)
        return True

    def displayStatus(self):
        """
        Displays every hedgehog's status
        """
        for hedgehog in self.player.hedgehogs:
            print(hedgehog.name)
            hedgehog.displayStatus()
        input("Press ENTER to continue: ")

    def canGetNewHedgehog(self):    
        """
        Determines if a hedgehog has max stats, meaning that the player gets a new hedgehog.
        Also makes sure that the player hasn't already got a new hedgheog from the hedgehog.
        """
        for hedgehog in self.player.hedgehogs:
            # Does the hedgehog have max status and can it produce a hedgehog?
            if hedgehog.isMaxStatus() and hedgehog.canGetNewHog == True and len(self.player.hedgehogs) < 5:
                name = input("You just got a new hedgehog! What will you name them? ")
                # Create new hedgehog and append them to player's hedgehog list
                newHedgehog = Hedgehog()
                newHedgehog.name = name
                self.player.hedgehogs.append(newHedgehog)
                # You can't get any more hedgehogs from this hedgehog
                hedgehog.canGetNewHog = False

    def canGetSpecialHog(self):
        """
        Determines if the user can get the final "Special" hedgehog
        """
        # Make sure they have 5 hedgehogs
        if len(self.player.hedgehogs) == 5:
            # Make sure all the hedgehogs have max status
            if (self.player.hedgehogs[0].isMaxStatus() 
                and self.player.hedgehogs[1].isMaxStatus()
                and self.player.hedgehogs[2].isMaxStatus() 
                and self.player.hedgehogs[3].isMaxStatus()
                and self.player.hedgehogs[4].isMaxStatus()):
                name = input("You just got a special hedgehog! What will you name them? ")
                # Create new hedgehog and append them to player's hedgehog list
                newHedgehog = SpecialHog()
                newHedgehog.name = name
                self.player.hedgehogs.append(newHedgehog)

    def win(self):
        """
        Determines if you won the game by maxing out your max hedgehog.
        """
        if len(self.player.hedgehogs) == 6 and self.player.hedgehogs[5].isSpecial and self.player.hedgehogs[5].isMaxStatus():
            print("You got your SPECIAL hedgehog to max status and won!")
            input("Select '8' on the menu to exit the game. [ENTER]")


    def update(self):
        """
        Things that need to happen every iteration of the game loop.
        """
        self.player.update()
        self.canGetNewHedgehog()
        self.canGetSpecialHog()
        self.win()