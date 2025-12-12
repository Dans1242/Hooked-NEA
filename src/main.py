import pygame
from player import Player
from shop import Shop

pygame.init()

player = Player()
shop = Shop()
gamescreen = pygame.display.set_mode((900, 550))


background = pygame.image.load("../assets/sprites/bg.png")
background = pygame.transform.scale(background, (900, 550)).convert()

pygame.display.set_caption("Hooked: Bestiary Odyssey")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    gamescreen.blit(background, (0, 0))
    player.movementUpdate()
    player.playerDraw(gamescreen)
    shop.shopDraw(gamescreen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()