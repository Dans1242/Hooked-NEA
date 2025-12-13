import pygame
import random

def RNG(loot):
    fishNames = list(loot.keys())
    fishChances = [info["chance"] for info in loot.values()]
    catch = random.choices(fishNames, weights=fishChances, k=1)[0]
    info = loot[catch]
    return (catch, info["rarity"], str(info['chance']*100)+"%", info["value"])