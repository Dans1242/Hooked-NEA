import pygame
import random
import json
import pygame_gui

clock = pygame.time.Clock()
pygame.init()

gamescreen = pygame.display.set_mode((900, 550))
pygame.display.set_caption("Hooked: Bestiary Odyssey")

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


my_sprite = MySprite(
    r"C:\Users\User\Documents\Hooked-Bestiary-Odyssey\assets\sprites\aibaby.jpeg",
    100,
    100
)

all_sprites = pygame.sprite.Group()
all_sprites.add(my_sprite)

running = True
speed = 6  # movement speed (pixels per frame)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- MOVEMENT HANDLING ---
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        my_sprite.move(0, -speed)
    if keys[pygame.K_s]:
        my_sprite.move(0, speed)
    if keys[pygame.K_a]:
        my_sprite.move(-speed, 0)
    if keys[pygame.K_d]:
        my_sprite.move(speed, 0)

    # --- DRAW EVERYTHING ---
    gamescreen.fill((0, 0, 0))          # clear screen
    all_sprites.draw(gamescreen)        # draw sprite
    pygame.display.flip()               # update display

    clock.tick(60)

pygame.quit()
