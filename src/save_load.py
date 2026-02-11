import json
import os
import pygame
from ui import Button

pygame.init()

titleBackground = pygame.image.load("../assets/sprites/titleBG.png")


def save_game(player, filename):
    save_data = {
        "inventory": player.inventory,
        "coins": player.coins
    }

    save_folder = os.path.dirname(filename)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(filename, "w") as fileToSave: #w means write mode
        json.dump(save_data, fileToSave)


def load_game(player, filename):
    if os.path.exists(filename):
        with open(filename, "r") as fileToLoad: #r means read mode
            save_data = json.load(fileToLoad)
            player.inventory = save_data.get("inventory", {})
            player.coins = save_data.get("coins", 0)
        return True
    else:
        print("No save file found.")
        return False
    

def pickSave(gamescreen):

    buttonImage = pygame.image.load("../assets/sprites/Button.png")
    font = pygame.font.Font(None, 32) # since its same font this saves time - just using this variable
    saveList = [file for file in os.listdir("saves") if file.endswith(".json")]
    
    saveSlots = []
    
    columns = 3
    startX, startY = 200, 150
    spacingX, spacingY = 250, 100

    # Generates grid of buttons
    for buttonInList, saveName in enumerate(saveList):
        if buttonInList >= 9: break #limit of 9
        
        displayName = saveName.removesuffix(".json")
        # Calculate grid position
        x = startX + (buttonInList % columns) * spacingX
        y = startY + (buttonInList // columns) * spacingY
        
        #Create each button
        saveSlotButton = Button(buttonImage, font, displayName, x, y, 0.2)
        
        saveSlots.append({"button": saveSlotButton, "path": "saves/" + displayName})

    # wait for use input with this while loop
    while True:
        mousePos = pygame.mouse.get_pos()
        gamescreen.fill((30, 30, 30))
        gamescreen.blit(titleBackground, (0, 0))

        #add ability to quit game at any time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for slot in saveSlots:
                    # Check if this specific button was clicked
                    if slot["button"].inputCheck(mousePos, event) == "clicked":
                        chosenSave = slot["path"]
                        return chosenSave # Returns the path and exits the function

        #draw buttons
        for slot in saveSlots:
            slot["button"].changeColour(mousePos)# calls the function to change the colour if mouse hovered
            slot["button"].drawButton(gamescreen)# itterates and draws each button in the list
            
        pygame.display.update()