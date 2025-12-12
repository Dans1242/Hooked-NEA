import pygame

class Shop:
    def __init__(self):
        self.sprite = pygame.image.load("../assets/sprites/shop.png")
        self.sprite = pygame.transform.scale(self.sprite, (300 * 1.35, 183 *1.35))
        self.xPos = 230
        self.yPos = -10

    def shopDraw(self, screen):
        screen.blit(self.sprite, (self.xPos, self.yPos))