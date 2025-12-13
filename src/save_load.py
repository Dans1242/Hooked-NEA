import json
import os

def save_game(player, filename="saves/save1.json"):
    save_data = {
        "inventory": player.inventory,
        "coins": player.coins
    }
    save_folder = os.path.dirname(filename)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    with open(filename, "w") as save_file: #w means write mode
        json.dump(save_data, save_file)

def load_game(player, filename="Save1.json"):
    if os.path.exists(filename):
        with open(filename, "r") as save_file: #r means read mode
            save_data = json.load(save_file)
            player.inventory = save_data.get("inventory", {})
            player.coins = save_data.get("coins", 0)