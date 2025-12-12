import pygame
import random

bestiary = {
    "Salmon" : {"rarity": "Common", "chance": 0.45, "value": 5},
    "Carp" : {"rarity": "Common", "chance": 0.4, "value": 6},
    "Cod" : {"rarity": "Rare", "chance": 0.25, "value": 12},
    "Tuna" : {"rarity": "Rare", "chance": 0.20, "value": 15},
    "Crab" : {"rarity": "Epic", "chance": 0.05, "value": 45},
    "Swordfish" : {"rarity": "Epic", "chance": 0.04, "value": 50},
    "Jellyfish" : {"rarity": "Legendary", "chance": 0.006, "value": 160},
    "Shark" : {"rarity": "Legendary", "chance": 0.006, "value": 170},
    "Whale" : {"rarity": "Mythic", "chance": 0.004, "value": 500},
    "Void Serpent" : {"rarity": "Secret", "chance": 0.001, "value": 2000},
}

fishNames = list(bestiary.keys())
fishRarities = [info["rarity"] for info in bestiary.values()]
fishChances = [info["chance"] for info in bestiary.values()]

fishRarityPairs = [(name, info["rarity"]) for name, info in bestiary.items()]

def RNG():
    return random.choice(fishNames, weights=fishChances)[0]
catch = RNG()
print(catch)
