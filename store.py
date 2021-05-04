"""
Describes a store where you can buy food.
Author: Benjamin Wyatt
"""

from food import Orange, Cake, Kibble


class Store:
    def __init__(self, player):
        # Item, price
        # self.inventory = {"Kibble" : 50, "Cake" : 100, "Orange" : 150}
        orange = Orange()
        cake = Cake()
        kibble = Kibble()
        self.inventory = [kibble, cake, orange]
        self.player = player

    def purchase(self):
        # Display players money
        print("You have ${}".format(self.player.money))
        # Display inventory
        print("Inventory:")
        for item in self.inventory:
            print(item.name, "${}".format(item.price))
        selection = input("Select item to purchase (press 'q' to exit): ").lower()
        # print("You selected {}!".format(selection))
        # Make sure input is valid
        while selection != "kibble" and selection != "cake" and selection != "orange" and selection != "q":
            selection = input("Please select a valid option: ")
        # Quit or make selection something that the list can use
        if selection == "q":
            return
        elif selection == "kibble":
            selection = 0
        elif selection == "cake":
            selection = 1
        else:
            selection = 2
        # If the player has enough money, subtract the price and give them the item
        if self.player.money >= self.inventory[selection].price:
            self.player.money -= self.inventory[selection].price
            self.player.food.append(self.inventory[selection])
            print("You purchased a/an {}!".format(self.inventory[selection].name))
        else:
            print("Sorry! You can't afford that item.\nEarn more money by washing and exercising your hedgehogs!")