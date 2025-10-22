import pygame
import random
import json
import pygame_gui

# initialize pygame
pygame.init()
gamescreen = pygame.display.set_mode((900,550))
# set window name to title
pygame.display.set_caption("Hooked: Bestiary Odyssey")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False