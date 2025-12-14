import pygame
import os
from player import Player
from shop import Shop
from RNG import RNG
from save_load import save_game, load_game, pickSave # imports functions needed for loading game, saving game, and picking/creating save slots

# Temporary loot tables listed below:

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

pygame.init() # initializing the game

player = Player()
shop = Shop()
gamescreen = pygame.display.set_mode((900, 550)) # setting the resolution (how big the window is)


background = pygame.image.load("../assets/sprites/bg.png") # retrieves the background's sprite
background = pygame.transform.scale(background, (900, 550)).convert() # scale the background to fit

pygame.display.set_caption("Hooked: Bestiary Odyssey")
clock = pygame.time.Clock()



chosenSave = pickSave()


# check if the save selected or created by the user exists in the saves folder
if os.path.exists(chosenSave):
    load_game(player, chosenSave)
    print("Game loaded successfully.")
# create a fresh slot if no slot found
else:
    player.inventory = {}
    player.coins = 0
    save_game(player, chosenSave)
    print("New save file created.")



# game loop
running = True
while running:   

    # shutting down + saving process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(player, chosenSave) # save the game using inventory and coin balance from player, at the current save
            print("Game saved successfully.")
            running = False

        # TEMPORARY "e" to fish
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_e:
                caughtFish = RNG(lootTable1) # generates a fish to be caught based on the paramater (lootTable1) i.e. gives a fish from the lootTable1

                print("You caught a " + caughtFish[0] + "! Rarity: " + caughtFish[1] + ", Chance: " + caughtFish[2] + ", Value: " + str(caughtFish[3]) + " coins")
                fishName = caughtFish[0]

                # checks if the fish already exists in the inventory, if so adds 1 to the count
                if fishName in player.inventory: 
                    player.inventory[fishName]["quantity"] += 1
                
                # if it doesnt exist it adds it along with the fish's info
                else:
                    player.inventory[fishName] = {
                        "quantity": 1,
                        "rarity": caughtFish[1],
                        "chance": caughtFish[2],
                        "value": caughtFish[3]
                    }
        

        # open inventory
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                print("Inventory:")
                for fishName, info in player.inventory.items():   
                    print(f"{info["quantity"]}x {fishName}")


        # sell fish
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                confirmation = input("Are you sure you want to sell all your fish? (y/n): ")   
                if confirmation.lower() == "y":
                    totalEarnings = shop.sellFish(player)
                    print(f"You sold all your fish for {totalEarnings} coins!")
                    player.coins += totalEarnings
                    print(f"You now have {player.coins} coins.")
                else:
                    print("Sale cancelled.")

        # check coin balance
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                print(f"You have {player.coins} coins.")


    player.movementUpdate()

    # draws the background, shop, and player every frame
    gamescreen.blit(background, (0, 0)) 
    shop.shopDraw(gamescreen)
    player.playerDraw(gamescreen)
    
    
    pygame.display.flip()
    clock.tick(60) # set FPS


pygame.quit()
