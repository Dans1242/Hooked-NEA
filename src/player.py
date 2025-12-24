import pygame
from RNG import RNG

class Player:
   def __init__(self):

      #misc
      self.direction = "right"
      self.xPos = 450
      self.yPos = 275
      self.speed = 5

      

      #sprites
      self.spriteRight = pygame.image.load("../assets/sprites/spriteRight.png")
      self.spriteRight = pygame.transform.scale(self.spriteRight, (12 * 5, 20 * 5))
      self.spriteLeft  = pygame.image.load("../assets/sprites/spriteLeft.png")
      self.spriteLeft = pygame.transform.scale(self.spriteLeft, (12 * 5, 20 * 5))
      self.spriteUp = pygame.image.load("../assets/sprites/spriteUp.png")
      self.spriteUp = pygame.transform.scale(self.spriteUp, (12 * 5, 20 * 5))
      self.spriteDown = pygame.image.load("../assets/sprites/spriteDown.png")
      self.spriteDown = pygame.transform.scale(self.spriteDown, (12 * 5, 20 * 5))
       
      #size
      self.image = self.spriteRight
      self.rect = self.image.get_rect(topleft=(self.xPos, self.yPos))

      self.inventory = {}

      self.coins = 0



   def movementUpdate(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w]:
         self.yPos -= self.speed
         self.direction = "up"
      elif keys[pygame.K_a]:
         self.xPos -= self.speed
         self.direction = "left"
      elif keys[pygame.K_s]:
         self.yPos += self.speed
         self.direction = "down"
      elif keys[pygame.K_d]:
         self.xPos += self.speed
         self.direction = "right"


   def updateCollisionRect(self):
      legHeight = self.rect.height * 0.25

      self.collisionRect = pygame.Rect(self.xPos + self.rect.width / 4, self.yPos + self.rect.height - legHeight, self.rect.width / 2, legHeight)
      return self.collisionRect




   def playerDraw(self, screen):
      if self.direction == "up":
         screen.blit(self.spriteUp, (self.xPos, self.yPos))
      elif self.direction == "down":
         screen.blit(self.spriteDown, (self.xPos, self.yPos))
      elif self.direction == "left":
         screen.blit(self.spriteLeft, (self.xPos, self.yPos))
      elif self.direction == "right":
         screen.blit(self.spriteRight, (self.xPos, self.yPos))
