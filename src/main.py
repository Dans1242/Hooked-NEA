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
                print("You caught a " + caughtFish[0] + "! Rarity: " + caughtFish[1] + ", Chance: " + caughtFish[2] + ", Value: " + str(caughtFish[3]) + " coins")
                fishName = caughtFish[0]
                if fishName in player.inventory:
                    player.inventory[fishName]["quantity"] += 1
                else:
                    player.inventory[fishName] = {
                        "quantity": 1,
                        "rarity": caughtFish[1],
                        "chance": caughtFish[2],
                        "value": caughtFish[3]
                    }
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                print("Inventory:")
                for fishName, info in player.inventory.items():   
                    print(f"{info['quantity']}x {fishName}")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                confirmation = input("Are you sure you want to sell all your fish? (y/n): ")   
                if confirmation.lower() == 'y':
                    totalEarnings = shop.sellFish(player)
                    print(f"You sold all your fish for {totalEarnings} coins!")
                else:
                    print("Sale cancelled.")

    player.movementUpdate()
    
    gamescreen.blit(background, (0, 0)) 
    shop.shopDraw(gamescreen)
    player.playerDraw(gamescreen)
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()