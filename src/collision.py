import pygame
from player import Player

blockedAreasBG1 = [
    # fd = forbidden direction
    {"rect": pygame.Rect(0, 0, 55, 550), "id": "leftBarrier", "fd": ["left"] },
    {"rect": pygame.Rect(0, 0, 950, 210), "id": "topBarrier","fd": ["up"] },
    {"rect": pygame.Rect(255, 0, 345, 240), "id": "shopBarrier", "fd": ["up", "left", "right"]},
    {"rect": pygame.Rect(0, 480, 900, 70), "id": "bottomBarrier", "fd": ["down"]},
    {"rect": pygame.Rect(750, 345, 200, 250), "id": "rightBarrier", "fd": ["right", "down"]}
    ]

blockedAreasBG2 = [
    
    {"rect": pygame.Rect(-50, 0, 950, 210), "id": "leftUpperBarrier", "fd": ["up"]},
    {"rect": pygame.Rect(-50, 345, 950, 250), "id": "leftLowerBarrier", "fd": ["down"]},
    {"rect": pygame.Rect(430, 210, 600, 135), "id": "seaBarrier", "fd": ["right"]}
    ]


def checkCollision(rect, blockedAreas):
    for area in blockedAreas:
        if rect.colliderect(area["rect"]):
            return area
    return None

def debugDrawBlockedAreas(gamescreen, bg2, background1, background2):
    if bg2:
        gamescreen.blit(background2, (0, 0))
        for blockedArea in blockedAreasBG2:
            pygame.draw.rect(gamescreen, (0, 0, 255), blockedArea["rect"], 2)
    else:
        gamescreen.blit(background1, (0, 0))
        for blockedArea in blockedAreasBG1:
            pygame.draw.rect(gamescreen, (0, 0, 255), blockedArea["rect"], 2)

