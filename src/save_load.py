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
    font = pygame.font.Font(None, 32)               # since its same font this saves time - just using this variable
    startX, startY = 200, 150
    spacingX, spacingY = 250, 100

    state = "grid"
    selectedSlot = None
    typedName = ""

    def buildGrid():        #function that will draw the buttons and refresh after a deleted save
        saveList = []
        for save in os.listdir("saves"):
            if save.endswith(".json"):
                saveList.append(save.removesuffix(".json"))     #stores name without the suffix so only the name is i the button

        while len(saveList) < 9:
            saveList.append(None) # this will make sure the grid is always filled even with no additional saves (will be used for the newsave)


        slots = []
        for i in range(9):
            column = i % 3
            x = startX + column * spacingX          # this will return one x coord for the current itterated button so for the first column column would be 0
                                                    # so 0 x spacing would just put the button at startX
            row = i // 3                            # same thing with y just with rows
            y = startY + row * spacingY

            name = saveList[i]      # fetches the name for the button its currently itterating through
            if name:                # if a name exists at this index saveList[i], thats the buttons display name
                displayName = name
            else:                   # otherwise if there is no name (in case of the list having None), the display name will be New Save
                displayName = "New Save"

            if name:
                path = "saves/" + name + ".json" # function needs to save the actual path for when the player presses delete button on the slot
            else:
                path = None

            #Button(image, font, textDisplayed, x, y, scale))
            button = Button(buttonImage, font, displayName, x, y, 0.2)
            slots.append({"button": button, "name": name, "path": path}) # adds all info into slots as a dictionary
            #the path uses an f string - and a condition - if there is a name or if the name is None (empty slot)

        return slots
    
    saveSlots = buildGrid()     # builds the grid once before the loop (that allows players to return to grid etc) starts

    # im just going to hardcode the 3 buttons that show after selecting a slot from a grid
    playButton = Button(buttonImage, font, "Play", 450, 200, 0.2)
    deleteButton = Button(buttonImage, font, "Delete", 450, 300, 0.2)
    returnButton = Button(buttonImage, font, "Return", 450, 400, 0.2)

    #begin a while loop for the different states
    while True:
        mousePos = pygame.mouse.get_pos()
        gamescreen.blit(titleBackground, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #--grid state
            if state == "grid":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for slot in saveSlots:
                        result = slot["button"].inputCheck(mousePos, event) # use inputcheck method from button class to return a result
                        if result == "clicked":
                            if slot["name"]: # if the slot has a name 
                                selectedSlot = slot
                                state = "selected"
                            else: # slot is None so have to go to naming screen
                                selectedSlot = slot
                                typedName = "" #have to clear any previous typing
                                state = "naming"

            #-- selected state (player clicked on save)
            elif state == "selected":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.inputCheck(mousePos, event) == "clicked":
                        return selectedSlot["path"] #return path to main.py to launch the game
                    
                    if deleteButton.inputCheck(mousePos, event) == "clicked":
                        os.remove(selectedSlot["path"])
                        saveSlots = buildGrid()             # refreshes the grid
                        state = "grid"                      # sends the player back to the grid state so they can choose another slot after deleting

                    if returnButton.inputCheck(mousePos, event) == "clicked":
                        state = "grid" # also returns player to grid state

            # -- naming state (uses on screen inputing rather than the input function using pygame key detection)
            elif state == "naming":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and typedName.strip(): # checks if player presses enter on a non empty name (not only spaces)
                        return f"saves/{typedName.strip()}.json" # returns the file path of the new save
                    
                    elif event.key == pygame.K_BACKSPACE:
                        typedName = typedName[:-1]
                    
                    elif event.key == pygame.K_ESCAPE:
                        state = "grid"

                    else:
                        if len(typedName) < 12:
                            typedName = typedName + event.unicode # adds the actal letter pressed to a string
        
        #-- code for drawing (only what belongs to each state)
        if state == "grid":
            for slot in saveSlots:
                slot["button"].changeColour(mousePos)
                slot["button"].drawButton(gamescreen)
        
        elif state == "selected":
            playButton.changeColour(mousePos)           # draw all 3 buttons in selected mode, as well as change the buttons colour when its hovered over it
            playButton.drawButton(gamescreen)
            deleteButton.changeColour(mousePos)
            deleteButton.drawButton(gamescreen)
            returnButton.changeColour(mousePos)
            returnButton.drawButton(gamescreen)
        
        elif state == "naming":
            promptText = font.render("Enter save name:", True, (255, 255, 255))
            nameText = font.render(typedName + "|", True, (255, 255, 0))
            gamescreen.blit(promptText, (300, 220))
            gamescreen.blit(nameText, (300, 270))

        pygame.display.update()