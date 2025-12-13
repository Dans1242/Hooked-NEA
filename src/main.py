import pygame
import os
from player import Player
from shop import Shop
from RNG import RNG
from save_load import save_game, load_game, pickSave

#loottables
lootTable1 = {
    "Salmon" : {"rarity": "Common", "chance": 0.45, "value": 5},
    "Carp" : {"rarity": "Common", "chance": 0.4, "value": 6},
    "Cod" : {"rarity": "Rare", "chance": 0.25, "value": 12},
    "Tuna" : {"rarity": "Rare", "chance": 0.20, "value": 15},
    "Crab" : {"rarity": "Epic", "chance": 0.05, "value": 45},
    "Swordfish" : {"rarity": "Epic", "chance": 0.04, "value": 50},
    "Jellyfish" : {"rarity": "Legendary", "chance": 0.006, "value": 160},
    "Shark" : {"rarity": "Legendary", "chance": 0.006, "value": 170},
    "Whale" : {"rarity": "Mythic", "chance": 0.004, "value": 500},
    "Void Serpent" : {"rarity": "Secret", "chance": 0.001, "value": 2000},
}

pygame.init()

player = Player()
shop = Shop()
gamescreen = pygame.display.set_mode((900, 550))


background = pygame.image.load("../assets/sprites/bg.png")
background = pygame.transform.scale(background, (900, 550)).convert()

pygame.display.set_caption("Hooked: Bestiary Odyssey")
clock = pygame.time.Clock()



chosenSave = pickSave()


if os.path.exists(chosenSave):
    load_game(player, chosenSave)
    print("Game loaded successfully.")
else:
    player.inventory = {}
    player.coins = 0
    save_game(player, chosenSave)
    print("New save file created.")


running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(player, chosenSave)
            print("Game saved successfully.")
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                caughtFish = RNG(lootTable1)
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
                    player.coins += totalEarnings
                    print(f"You now have {player.coins} coins.")
                else:
                    print("Sale cancelled.")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print(f"You have {player.coins} coins.")


    player.movementUpdate()
    
    gamescreen.blit(background, (0, 0)) 
    shop.shopDraw(gamescreen)
    player.playerDraw(gamescreen)
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()