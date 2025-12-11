import pygame

class Player:
   def __init__(self):
      self.spriteRight = pygame.image.load(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\spriteRight.png")
      self.spriteLeft = pygame.image.load(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\spriteLeft.png")
      #self.spriteUp = pygame.image.load(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\spriteUp.png")
      #self.spriteDown = pygame.image.load(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\spriteDown.png")
      self.spriteFront = pygame.image.load(r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\spriteFront.png")

      
        
      self.xPos = 450
      self.yPos = 275
      self.speed = 5


   def movementUpdate(self):
      self.direction = "front"
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

   def playerDraw(self, screen):
      if self.direction == "up":
         screen.blit(self.spriteUp, (self.xPos, self.yPos))
      elif self.direction == "down":
         screen.blit(self.spriteDown, (self.xPos, self.yPos))
      elif self.direction == "left":
         screen.blit(self.spriteLeft, (self.xPos, self.yPos))
      elif self.direction == "right":
         screen.blit(self.spriteRight, (self.xPos, self.yPos))
      elif self.direction == "front":
         screen.blit(self.spriteFront, (self.xPos, self.yPos))