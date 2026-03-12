from tkinter import font
import pygame
import os
from player import Player
from shop import Shop
from RNG import RNG
from save_load import save_game, load_game, pickSave # imports functions needed for loading game, saving game, and picking/creating save slots
from collision import blockedAreasBG1, blockedAreasBG2, checkCollision
from ui import Button
from collections import deque

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

raritySettings = {
    "Common":    {"clicks": 3, "window": 3.0,  "colour": (255, 255, 255)},  # white
    "Uncommon":  {"clicks": 3, "window": 2.5,  "colour": (0, 255, 0)},      # green
    "Rare":      {"clicks": 3, "window": 2.0,  "colour": (0, 100, 255)},    # blue
    "Epic":      {"clicks": 3, "window": 1.5,  "colour": (255, 192, 203)},    # pink
    "Legendary": {"clicks": 3, "window": 1.0,  "colour": (255, 215, 0)},    # gold
    "Mythic":    {"clicks": 3, "window": 0.8,  "colour": (128, 0, 128)},    # purple
    "Secret":    {"clicks": 3, "window": 0.5,  "colour": (0, 0, 0)},    # black
}

pygame.init() # initializing the game

player = Player()
shop = Shop()
gamescreen = pygame.display.set_mode((900, 550)) # setting the resolution (how big the window is)


titleBackground = pygame.image.load("../assets/sprites/titleBG.png")
background1 = pygame.image.load("../assets/sprites/bg.png") # retrieves the background's sprite
background1 = pygame.transform.scale(background1, (900, 550)).convert() # scale the background to fit
background2 = pygame.image.load("../assets/sprites/bg2.png") # retrieves the pier backround
background2 = pygame.transform.scale(background2, (900, 550)).convert() # scale the background to fit
buttonImage = pygame.image.load("../assets/sprites/Button.png")


pygame.display.set_caption("Hooked: Bestiary Odyssey")
clock = pygame.time.Clock()



# game loop
def play(chosenSave):
    

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
    
    running = True
    bg2 = False
    debugMode = False
    showInventory = False
    showShop = False
    shopMessage = ""
    shopResult = ""
    shopResultTime = 0

    # - setting up fishing minigame variables - #
    fishingState = "idle"
    castTime = 0
    minigameStartTime = 0
    requiredClicks = 0
    clickWindow = 0
    clickCount = 0
    pendingFish = None
    exclamationColour = (255, 255, 255)
    # - end of fishing variables #

    fishMessages = deque()

    font = pygame.font.SysFont("arial", 24, bold=True) #large font for UI elements
    smallFont = pygame.font.SysFont("arial", 18) # smaller font for inventory items etc
    exclamationFont = pygame.font.SysFont("arial", 75, bold=True)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #save and quit
                save_game(player, chosenSave) # save the game using inventory and coin balance from player, at the current save
                print("Game saved successfully.")
                running = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e: #fishing
                    if bg2 and player.xPos > 300 and player.xPos < 600:  
                        if fishingState == "idle":
                            fishingState = "casting"
                            castTime = pygame.time.get_ticks()
                            pendingFish = RNG(tempLootTable) # generates a fish to be caught based on the paramater (lootTable1) i.e. gives a fish from the lootTable1
                    else:
                        print("You can't fish here! Go to the pier to fish.")
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i: #check inventory
                    showInventory = not showInventory


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: #sell fish
                    if player.xPos > 300 and player.xPos < 600 and not bg2: #checks if the player is near the shop
                        showShop = not showShop
                        shopMessage = "Welcome to the shop. Press Y to sell all your fish, or N to cancel."

                if event.key == pygame.K_y:
                    if showShop:
                        earnings = shop.sellFish(player)
                        player.coins += earnings
                        shopResult = f"You sold all your fish for {earnings} coins!"
                        shopResultTime = pygame.time.get_ticks() # gets the current time in milliseconds
                        shopMessage = ""
                        showShop = False

                if event.key == pygame.K_n:
                    if showShop:                
                        shopResult = "Sale cancelled. Come back anytime :)"
                        shopResultTime = pygame.time.get_ticks() # gets the current time in milliseconds
                        shopMessage = ""
                        showShop = False

            if event.type == pygame.MOUSEBUTTONDOWN: # checks for a mouse click
                if fishingState == "minigame":
                    clickCount += 1 # adds click everytime the player clicks
                    if clickCount >= requiredClicks:
                        fishingState = "idle" # completes the minigame and resets state
                        fishName = pendingFish[0]
                        fishMessages.append({"text": f"You caught a {fishName}!", "time": pygame.time.get_ticks()}) # adds caught fish and time it was caught to the list to be displayed
                        if fishName in player.inventory: #inventory system
                            player.inventory[fishName]["quantity"] += 1
                        else:
                            player.inventory[fishName] = {
                                "quantity": 1,
                                "rarity": pendingFish[1],
                                "chance": pendingFish[2],
                                "value": pendingFish[3]
                            }
                        pendingFish = None # resets pending fish after catching



            if event.type == pygame.KEYDOWN and event.key == pygame.K_b: #check coin balance
                    print(f"You have {player.coins} coins.")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_F3: #toggle debug mode
                debugMode = not debugMode

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

        
        # -- DRAWING SETION -- #
        
        if bg2:
            gamescreen.blit(background2, (0, 0))
            if debugMode:
                for blockedArea in blockedAreasBG2:
                    pygame.draw.rect(gamescreen, (0, 0, 255), blockedArea["rect"], 2)
        else:
            gamescreen.blit(background1, (0, 0))
            shop.shopDraw(gamescreen)
            if debugMode:
                for blockedArea in blockedAreasBG1:
                    pygame.draw.rect(gamescreen, (0, 0, 255), blockedArea["rect"], 2)
            
        player.playerDraw(gamescreen) #draw player
        player.updateCollisionRect() #updates player collision box

        # coin balance display
        coinUI = font.render(f"Coins: {player.coins}", True, (255, 255, 0))
        gamescreen.blit(coinUI, (10, 10))

        if debugMode: #draws the red collision box around the player for debugging
            pygame.draw.rect(gamescreen, (255, 0, 0), player.collisionRect, 2)
        
        if showInventory:
            inventoryPanel = pygame.Surface((200, 350)) # creates a surface for the inventory panel
            inventoryPanel.set_alpha(200) # set transparency
            inventoryPanel.fill((50, 50, 50)) # dark grey background
            gamescreen.blit(inventoryPanel, (10, 50))

            inventoryTitle = font.render("Inventory:", True, (255, 255, 255))
            gamescreen.blit(inventoryTitle, (20, 60))
            space = 100
            for item, quantity in player.inventory.items():
                itemText = smallFont.render(f"{item} x{quantity['quantity']}", True, (255, 255, 255))
                gamescreen.blit(itemText, (20, space))
                space += 25

        if showShop:
            shopText = smallFont.render(shopMessage, True, (255, 255, 255))
            gamescreen.blit(shopText, (200, 500))

        if shopResult and not showShop:
            if pygame.time.get_ticks() - shopResultTime < 2000: # result dissapears after 2 seconds
                resultText = smallFont.render(shopResult, True, (255, 255, 255))
                gamescreen.blit(resultText, (200, 500))
            else:
                shopResult = "" # clear result after 2seconds

        if fishMessages:
            while fishMessages and pygame.time.get_ticks() - fishMessages[0]["time"] > 2000: # current live time minus the time fish was caught
                fishMessages.popleft() # removes the message from the queue
            
            yOffset = 0
            for i in fishMessages:
                messageText = smallFont.render(i["text"], True, (255, 255, 255)) # using small white text for the fish message
                gamescreen.blit(messageText, (player.xPos, player.yPos - 30 - yOffset)) # draw the actial message
                yOffset += 20 # offset for each message above eachother

        if fishingState == "casting":
            if pygame.time.get_ticks() - castTime > 500: # makes the player wait 5 seconds after casting before fish bites
                fishingState = "warning"
                minigameStartTime = pygame.time.get_ticks()
                rarity = pendingFish[1] # fethecs rarity from the randomised fish
                clickWindow = raritySettings[rarity]["window"] * 1000 # grabs click window depending on fish rarirty
                requiredClicks = raritySettings[rarity]["clicks"] # grabs required clicks depending on fish rarity
                clickCount = 0
                exclamationColour = raritySettings[rarity]["colour"] # grabs the colour for the exclamation mark depending on rarity
            else:
                castText = font.render("Casting...", True, (255, 255, 255))
                gamescreen.blit(castText, (player.xPos - 20, player.yPos - 30))

        if fishingState == "warning":
            exclamationText = exclamationFont.render("!", True, (exclamationColour))
            gamescreen.blit(exclamationText, (player.xPos + 15, player.yPos - 60))
            if pygame.time.get_ticks() - minigameStartTime > 2000: # ! lasts for 2 seconds
                fishingState = "minigame"
                minigameStartTime = pygame.time.get_ticks() #resets the timer for click window

        if fishingState == "minigame":
            timeLeft = clickWindow - (pygame.time.get_ticks() - minigameStartTime)# calculates time left for when the player can click
            if timeLeft <= 0:
                
                # TIME RUNS OUT
                fishingState = "idle"
                fishMessages.append({"text": f"The {pendingFish[0]} got away...", "time": pygame.time.get_ticks()})
                pendingFish = None
            else:
                # draw click counter and time left
                clickText = smallFont.render(f"Clicks: {clickCount}/{requiredClicks}", True, (255, 255, 255))
                timeText = smallFont.render(f"{timeLeft / 1000:.1f}s", True, (255, 255, 255))
                gamescreen.blit(clickText, (player.xPos - 20, player.yPos - 70))
                gamescreen.blit(timeText, (player.xPos - 20, player.yPos - 90))

        pygame.display.flip()
        clock.tick(60) # set FPS


    pygame.quit()

def titleScreen():
    pygame.display.set_caption("Hooked: Bestiary Odyssey - Title Screen")

    titleFont = pygame.font.SysFont("arial", 128, bold=True)
    subTitleFont = pygame.font.SysFont("arial", 32)
    titleText = titleFont.render("Hooked", True, (209, 142, 61))
    subTitleText = subTitleFont.render("Bestiary Odyssey", True, (255, 255, 255))
    
    #Button(image, font, textDisplayed, x, y, scale))
    playButton = Button(buttonImage, pygame.font.Font(None, 32), "Play", 450, 300, 0.2) # instance of button class as play button
    playPressed = False
    
    chosenSave = None
    while playPressed == False:
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if playButton.inputCheck(mousePos, event) == "clicked":
                chosenSave = pickSave(gamescreen) # brings you to a 9 box selection
                playPressed = True
        
        #code concerning play button
        gamescreen.blit(titleBackground, (0, 0))
        gamescreen.blit(titleText, (220, 75))
        gamescreen.blit(subTitleText, (325, 200))
        playButton.changeColour(mousePos) #hover effect
        playButton.drawButton(gamescreen)
        pygame.display.flip()
    return chosenSave

chosenSave = titleScreen()
play(chosenSave)