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

def RNG():
    catch = random.choices(fishNames, weights=fishChances, k=1)[0]
    info = bestiary[catch]
    return (catch, info["rarity"], str(info["chance"]*100) + "%", info["value"])
