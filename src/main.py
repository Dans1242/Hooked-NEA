import pygame

pygame.init()

gamescreen = pygame.display.set_mode((900, 550))
pygame.display.set_caption("Hooked: Bestiary Odyssey")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")
        if event.type == pygame.KEYUP:
            print(f"Key released: {pygame.key.name(event.key)}")

    gamescreen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
