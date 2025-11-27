import pygame
import random
import json
import pygame_gui

clock = pygame.time.Clock()
pygame.init()

gamescreen = pygame.display.set_mode((900, 550))
pygame.display.set_caption("Hooked: Bestiary Odyssey")

class character(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, changeInX, changeInY):
        self.rect.x += changeInX
        self.rect.y += changeInY


playerSprite = character(
    r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\characterIdle.png",
    100,
    100
)

all_sprites = pygame.sprite.Group()
all_sprites.add(playerSprite)

running = True
speed = 6  # movement speed (pixels per frame)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    wasd = pygame.key.get_pressed()

    if wasd[pygame.K_w]:
        playerSprite.move(0, -speed)
    if wasd[pygame.K_s]:
        playerSprite.move(0, speed)
    if wasd[pygame.K_a]:
        playerSprite.move(-speed, 0)
    if wasd[pygame.K_d]:
        playerSprite.move(speed, 0)

    gamescreen.fill((0, 0, 0))          # clears the screen
    all_sprites.draw(gamescreen)        # draws the sprite
    pygame.display.flip()               # update the display

    clock.tick(60) # set fps

pygame.quit()
