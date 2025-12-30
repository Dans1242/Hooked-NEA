import pygame


pygame.init()

class Button:
    def __init__(self, image, font, textDisplayed, x, y, scale):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.font = font
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y)) #creates a rect for the image of the button
        self.textDisplayed = textDisplayed
        self.text = font.render(self.textDisplayed, True, "white")
        self.textRect = self.text.get_rect(center=self.rect.center) #creates a rect for the text in the button

    def drawButton(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    def inputCheck(self, mousePos, event=None):
        hovered = self.rect.collidepoint(mousePos)

        if event and event.type == pygame.MOUSEBUTTONDOWN and hovered: #if clicked while hovered
            return "clicked"
        if hovered:
            return "hovered"
        
        return None
    
    def changeColour(self, mousePos):
        hovered = self.rect.collidepoint(mousePos)
        if hovered:
            self.text = self.font.render(self.textDisplayed, True, "green")
        else:
            self.text = self.font.render(self.textDisplayed, True, "white")