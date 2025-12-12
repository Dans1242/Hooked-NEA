import pygame
import random

bestiary = {
    "Salmon" : {"rarity": "Common", "chance": 0.45, "value": 5},
    "Carp" : {"rarity": "Common", "chance": 0.4, "value": 5},
    "Cod" : {"rarity": "Rare", "chance": 0.25, "value": 5},
    "Tuna" : {"rarity": "Rare", "chance": 0.20, "value": 5},
    "Crab" : {"rarity": "Epic", "chance": 0.05, "value": 5},
    "Swordfish" : {"rarity": "Epic", "chance": 0.04, "value": 5},
    "Jellyfish" : {"rarity": "Legendary", "chance": 0.006, "value": 5},
    "Shark" : {"rarity": "Legendary", "chance": 0.006, "value": 5},
    "Whale" : {"rarity": "Mythic", "chance": 0.004, "value": 5},
    "Void Serpent" : {"rarity": "Secret", "chance": 0.001, "value": 5},
}

fishCaught = random.choice()