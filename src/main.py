import pygame
from player import Player

pygame.init()

player = Player()
gamescreen = pygame.display.set_mode((900, 550))
pygame.display.set_caption("Hooked: Bestiary Odyssey")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    gamescreen.fill((0, 0, 0))
    player.movementUpdate()
    player.playerDraw(gamescreen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
