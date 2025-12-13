import json
import os
import pygame

pygame.init()





def save_game(player, filename):
    save_data = {
        "inventory": player.inventory,
        "coins": player.coins
    }

    save_folder = os.path.dirname(filename)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(filename, "w") as fileToSave: #w means write mode
        json.dump(save_data, fileToSave)





def load_game(player, filename):
    if os.path.exists(filename):
        with open(filename, "r") as fileToLoad: #r means read mode
            save_data = json.load(fileToLoad)
            player.inventory = save_data.get("inventory", {})
            player.coins = save_data.get("coins", 0)
        return True
    else:
        print("No save file found.")
        return False
    




def pickSave():
    saveList = [file for file in os.listdir("saves") if file.endswith(".json")]

    for save in enumerate(saveList):
        print(f"{save[0]+1}. {save[1]}")
    chosenSave = input("Enter the number of the save you want to load, or 'n' to create a new save: ")
    if chosenSave.isdigit() and 1 <= int(chosenSave) <= len(saveList):
        chosenSave = "saves/" + saveList[int(chosenSave)-1]
    elif chosenSave.lower() == 'n':
        chosenSave = "saves/" + input("Enter a name for your new save file: ") + ".json"
    return chosenSave