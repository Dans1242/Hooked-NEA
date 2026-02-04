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
    font = pygame.font.Font(None, 32)
    saveList = [file for file in os.listdir("saves") if file.endswith(".json")]
    
    save_slots = []
    
    # Grid code
    columns = 3
    start_x, start_y = 200, 150
    spacing_x, spacing_y = 250, 100

    #Generates grid of buttons
    for index, save_name in enumerate(saveList):
        if index >= 9: break #limit of 9
        
        displayName = save_name.removesuffix(".json")
        # Calculate grid position
        x = start_x + (index % columns) * spacing_x
        y = start_y + (index // columns) * spacing_y
        
        #Create each button
        saveSlotButton = Button(buttonImage, font, displayName, x, y, 0.2)
        
        # Store as a pair so we know which file belongs to which button
        save_slots.append({"button": saveSlotButton, "path": "saves/" + displayName})

    # 2. The Loop: Wait for the user to pick one
    while True:
        mouse_pos = pygame.mouse.get_pos()
        gamescreen.fill((30, 30, 30))
        gamescreen.blit(titleBackground, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for slot in save_slots:
                    # Check if this specific button was clicked
                    if slot["button"].inputCheck(mouse_pos, event) == "clicked":
                        chosenSave = slot["path"]
                        return chosenSave # Returns the path and exits the function

        # 3. Update and Draw
        for slot in save_slots:
            slot["button"].changeColour(mouse_pos)
            slot["button"].drawButton(gamescreen)
            
        pygame.display.update()