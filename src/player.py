import pygame

class playerClass(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move(self, changeInX, changeInY):
        self.rect.x += changeInX
        self.rect.y += changeInY
    
    def inputHandler(self):
        wasd = pygame.key.get_pressed()

        if wasd[pygame.K_w]:
            self.move(0, -self.speed)
        if wasd[pygame.K_s]:
            self.move(0, self.speed)
        if wasd[pygame.K_a]:
            self.move(-self.speed, 0)
        if wasd[pygame.K_d]:
            self.move(self.speed, 0)