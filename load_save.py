"""
Functions to save and load the program.
Author: Benjamin Wyatt
"""
import json

def save(player):
    """
    Saves the players data into a json file.
    """

    numKibble = 0
    numCake = 0
    numOrange = 0
    for food in player.food:
        if food.name == "Kibble":
            numKibble += 1
        elif food.name == "Cake":
            numCake += 1
        elif food.name == "Orange":
            numOrange += 1

    data = {
        "player" : [
            {
            "name" : player.name,
            "money" : player.money,
            "numKibble" : numKibble,
            "numCake" : numCake,
            "numOrange" : numOrange,
            "numHedgehogs" : len(player.hedgehogs)
            }
        ],
    }

    data["hedgehogs"] = []

    for hedgehog in player.hedgehogs:
        data["hedgehogs"].append({
            "name" : hedgehog.name,
            "hunger" : hedgehog.hunger,
            "health" : hedgehog.health,
            "hygiene" : hedgehog.hygiene,
            "canGetNewHog" : hedgehog.canGetNewHog,
            "isSpecial" : hedgehog.isSpecial
        })

    with open("save.json", "w") as outfile:
        json.dump(data, outfile, indent=4)



def load(player):
    """
    Loads save data into the game.
    """
    # Open and load the json file
    with open("save.json") as save:
        save_data = json.load(save)

        # Get the player data and initialize it
        for data in save_data["player"]:
            player.name = data["name"]
            player.money = data["money"]
            player.initializeFood(data["numKibble"], data["numCake"], data["numOrange"])

        # Get the hedgehog data and initialize it
        for data in save_data["hedgehogs"]:
            player.initializeHedgehogs(data["name"], data["hunger"], data["health"],
                                       data["hygiene"], data["canGetNewHog"], data["isSpecial"])