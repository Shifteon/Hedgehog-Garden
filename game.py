from hedgehog import Hedgehog
from food import Food, Orange, Kibble, Cake
from player import Player

class Game:
    def __init__(self, name):
        self.player = Player(name)
    

    def getInput(self, min, max): 
        """
        Function to recieve integer input.
        Enter a minimum value and a max value.
        """
        selection = int(input())
        while selection < min or selection > max:
            selection = int(input("Please input a valid option: "))
        return selection

    def displayHedgehogs(self):
        pass

    def displayFood(self):
        pass

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
        print("7 - Quit")
        selection = self.getInput(1, 7)
        if selection == 1:
            self.displayHedgehogs()
        elif selection == 2:
            self.displayStatus()
        elif selection == 3:
            self.displayFood()
        elif selection == 4:
            for hedgehog in self.player.hedgehogs:
                orange = Orange()
                hedgehog.feed(orange)
        elif selection == 5:
            for hedgehog in self.player.hedgehogs:
                hedgehog.wash()
        elif selection == 6:
            pass
        elif selection == 7:
            return False
        return True

    def displayStatus(self):
        for hedgehog in self.player.hedgehogs:
            print(hedgehog.name)
            hedgehog.displayStatus()
        input("Press any ENTER to continue: ")

    def canGetNewHedgehog(self):    
        for hedgehog in self.player.hedgehogs:
            if hedgehog.isMaxStatus():
                newHedgehog = Hedgehog()
                self.player.hedgehogs.append(newHedgehog)

    def getNewHedgehog(self):
        pass

    def update(self):
        self.canGetNewHedgehog()