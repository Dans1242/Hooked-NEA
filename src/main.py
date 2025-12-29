import pygame
import os
from player import Player
from shop import Shop
from RNG import RNG
from save_load import save_game, load_game, pickSave # imports functions needed for loading game, saving game, and picking/creating save slots
from collision import blockedAreasBG1, blockedAreasBG2, checkCollision

# Temporary loot tables listed below:

#lootTable1 = {
#    "Salmon" : {"rarity": "Common", "chance": 0.45, "value": 5},
#    "Carp" : {"rarity": "Common", "chance": 0.4, "value": 6},
#    "Cod" : {"rarity": "Rare", "chance": 0.25, "value": 12},
#    "Tuna" : {"rarity": "Rare", "chance": 0.20, "value": 15},
#    "Crab" : {"rarity": "Epic", "chance": 0.05, "value": 45},
#    "Swordfish" : {"rarity": "Epic", "chance": 0.04, "value": 50},
#    "Jellyfish" : {"rarity": "Legendary", "chance": 0.006, "value": 160},
#    "Shark" : {"rarity": "Legendary", "chance": 0.006, "value": 170},
#    "Whale" : {"rarity": "Mythic", "chance": 0.004, "value": 500},
#    "Void Serpent" : {"rarity": "Secret", "chance": 0.001, "value": 2000},
#}

tempLootTable = {
    # Common – bread and butter fish
    "Minnow": {"rarity": "Common", "chance": 0.30, "value": 2},
    "Carp": {"rarity": "Common", "chance": 0.25, "value": 5},
    "Salmon": {"rarity": "Common", "chance": 0.20, "value": 7},
    "Herring": {"rarity": "Common", "chance": 0.15, "value": 6},

    # Uncommon – slightly exciting
    "Trout": {"rarity": "Uncommon", "chance": 0.12, "value": 10},
    "Bass": {"rarity": "Uncommon", "chance": 0.10, "value": 12},

    # Rare – feels rewarding
    "Cod": {"rarity": "Rare", "chance": 0.07, "value": 20},
    "Tuna": {"rarity": "Rare", "chance": 0.06, "value": 25},

    # Epic – big moments
    "Swordfish": {"rarity": "Epic", "chance": 0.03, "value": 80},
    "Giant Crab": {"rarity": "Epic", "chance": 0.025, "value": 90},

    # Legendary – memorable catches
    "Great White Shark": {"rarity": "Legendary", "chance": 0.01, "value": 250},
    "Moon Jellyfish": {"rarity": "Legendary", "chance": 0.008, "value": 220},

    # Mythic – very rare, very valuable
    "Ancient Whale": {"rarity": "Mythic", "chance": 0.004, "value": 600},

    # Secret – flex items, not expected
    "Abyssal Serpent": {"rarity": "Secret", "chance": 0.001, "value": 2000}
}

pygame.init() # initializing the game

player = Player()
shop = Shop()
gamescreen = pygame.display.set_mode((900, 550)) # setting the resolution (how big the window is)
bg2 = False


background1 = pygame.image.load("../assets/sprites/bg.png") # retrieves the background's sprite
background1 = pygame.transform.scale(background1, (900, 550)).convert() # scale the background to fit
background2 = pygame.image.load("../assets/sprites/bg2.png") # retrieves the pier backround
background2 = pygame.transform.scale(background2, (900, 550)).convert() # scale the background to fit


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
                if bg2 and player.xPos > 300 and player.xPos < 600:    
                    caughtFish = RNG(tempLootTable) # generates a fish to be caught based on the paramater (lootTable1) i.e. gives a fish from the lootTable1

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
                else:
                    print("You can't fish here! Go to the pier to fish.")
        




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


    # background switch
    if player.xPos > 900 and not bg2:
        player.xPos = 0
        bg2 = not bg2
    elif player.xPos < 0 and bg2:
        player.xPos = 900
        bg2 = not bg2

    # input desired movement
    player.desiredMovement()

    # x movement and collision check
    player.xPos += player.xVel
    player.updateCollisionRect()

    hit = checkCollision(player.collisionRect, blockedAreasBG2 if bg2 else blockedAreasBG1)
    if hit:
        fd = hit["fd"]

        if player.xVel > 0 and "right" in fd:
            player.xPos -= player.xVel
        elif player.xVel < 0 and "left" in fd:
            player.xPos -= player.xVel

    # y movement and collision check
    player.yPos += player.yVel
    player.updateCollisionRect()

    hit = checkCollision(player.collisionRect, blockedAreasBG2 if bg2 else blockedAreasBG1)
    if hit:
        fd = hit["fd"]
        if player.yVel > 0 and "down" in fd:
            player.yPos -= player.yVel
        elif player.yVel < 0 and "up" in fd:
            player.yPos -= player.yVel






    # draws the background, shop, and player every frame
    if bg2:
        gamescreen.blit(background2, (0, 0))
        for blockedArea in blockedAreasBG2:
            pygame.draw.rect(gamescreen, (0, 0, 255), blockedArea["rect"], 2)
    else:
        gamescreen.blit(background1, (0, 0))
        shop.shopDraw(gamescreen)
        for blockedArea in blockedAreasBG1:
            pygame.draw.rect(gamescreen, (0, 0, 255), blockedArea["rect"], 2)
    
    player.playerDraw(gamescreen)
    player.updateCollisionRect()
    pygame.draw.rect(gamescreen, (255, 0, 0), player.collisionRect, 2)
    
    
    pygame.display.flip()
    clock.tick(60) # set FPS


pygame.quit()
