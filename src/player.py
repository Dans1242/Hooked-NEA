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

      #data
      self.inventory = {}
      self.coins = 0
      self.lureSpeed = 1
      self.luck = 1
      self.valueBoost = 1


   def desiredMovement(self):
      keys = pygame.key.get_pressed()

      self.xVel = 0
      self.yVel = 0

      if keys[pygame.K_a]:
         self.xVel = -self.speed
         self.direction = "left"
      if keys[pygame.K_d]:
         self.xVel = +self.speed
         self.direction = "right"
      if keys[pygame.K_w]:
         self.yVel = -self.speed
         self.direction = "up"
      if keys[pygame.K_s]:
         self.yVel = +self.speed
         self.direction = "down"

      # normalise diagonal movement
      if self.xVel != 0 and self.yVel != 0:
         self.xVel *= 0.7071 # 1/sqrt(2)
         self.yVel *= 0.7071



   def updateCollisionRect(self):
      legHeight = self.rect.height * 0.25

      self.collisionRect = pygame.Rect(self.xPos + self.rect.width / 4, self.yPos + self.rect.height - legHeight, self.rect.width / 2, legHeight)
      return self.collisionRect

   def buyUpgrade(self, upgrade, cost):
      if self.coins >= cost:
         self.coins -= cost
         #setattr(self, upgrade, (value to set it to) )
         setattr(self, upgrade, getattr(self, upgrade) + 1)
         return True
      return False


   def playerDraw(self, screen):
      if self.direction == "up":
         screen.blit(self.spriteUp, (self.xPos, self.yPos))
      elif self.direction == "down":
         screen.blit(self.spriteDown, (self.xPos, self.yPos))
      elif self.direction == "left":
         screen.blit(self.spriteLeft, (self.xPos, self.yPos))
      elif self.direction == "right":
         screen.blit(self.spriteRight, (self.xPos, self.yPos))
