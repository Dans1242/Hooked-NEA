import pygame
from player import Player

blockedAreasBG1 = [
    #pygame.Rect(x, y, width, height)
    pygame.Rect(0, 0, 55, 550), # left barrier
    pygame.Rect(0, 0, 900, 210), # top barrier
    pygame.Rect(255, 0, 345, 240), # shop barrier
    pygame.Rect(0, 480, 900, 70), # bottom barrier
    pygame.Rect(750, 345, 150, 250) # right barrier
    ]

blockedAreasBG2 = [
    #pygame.Rect(x, y, width, height)
    pygame.Rect(0, 0, 900, 210), # left upper barrier
    pygame.Rect(0, 345, 900, 250), # left lower barrier
    pygame.Rect(430, 210, 600, 135) # sea barrier
    ]
