import pygame
import random
import json
import pygame_gui


#create a clock variable
clock = pygame.time.Clock()

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
        # check for when a key is pressed down and print which key was pressed down
        if event.type == pygame.KEYDOWN()
            print(f"Key pressed: {pygame.key.name(event.key)}")
        # check which key was released and print it
        if event.type == pygame.KEYUP()
            print(f"Key released: {pygame.key.name(event.key)}")
    
    clock.tick(60)
