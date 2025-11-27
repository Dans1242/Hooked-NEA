import pygame
import random
import json
import pygame_gui

from player import playerClass

pygame.init()
clock = pygame.time.Clock()

gamescreen = pygame.display.set_mode((900, 550))
pygame.display.set_caption("Hooked: Bestiary Odyssey")


characterIdleRight = playerClass(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\characterIdleRight.png", 100, 100)
characterIdleLeft = playerClass(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\characterIdleLeft.png", 100, 100)

characterSprites = pygame.sprite.Group()
characterSprites.add(characterIdleRight)
characterSprites.add(characterIdleLeft)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    playerClass.inputHandler(characterIdleRight)
    
    gamescreen.fill((0, 0, 0))
    characterSprites.draw(gamescreen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
