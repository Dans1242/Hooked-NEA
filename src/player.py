import pygame

class Player:
    def __init__(self):
        self.playerSprite = pygame.image.load(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\characterIdleRight.png")
        self.xPos = 450
        self.yPos = 275
        self.speed = 5


    def movementUpdate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
           self.yPos -= self.speed
           print(self.yPos)
        if keys[pygame.K_a]:
           self.xPos -= self.speed
           print(self.xPos)
        if keys[pygame.K_s]:
           self.yPos += self.speed
           print(self.yPos)
        if keys[pygame.K_d]:
           self.xPos += self.speed
           print(self.xPos)


    def playerDraw(self, screen):
       screen.blit(self.playerSprite, (self.xPos, self.yPos))
