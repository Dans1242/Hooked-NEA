import pygame
from player import Player
from shop import Shop
from RNG import RNG

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                caughtFish = RNG()
                player.inventory.append(caughtFish)
                print(f"Congratulations! You caught a {caughtFish[0]} ({caughtFish[1]}) worth {caughtFish[3]} coins! (Chance: {caughtFish[2]})")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                print("Inventory:")
                for item in player.inventory:
                    print(f"- {item[0]} ({item[1]}) worth {item[3]} coins (Chance: {item[2]})")

    player.movementUpdate()
    
    gamescreen.blit(background, (0, 0)) 
    shop.shopDraw(gamescreen)
    player.playerDraw(gamescreen)
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()