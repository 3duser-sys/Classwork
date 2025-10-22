import pygame

pygame.init()
windows = pygame.display.set_mode((800, 600))
GREEN = (0, 255, 0)
pygame.draw.circle(windows, GREEN, (300, 300), 50)
pygame.draw.circle(windows, GREEN, (100, 100), 50, 3)

pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

pygame.quit()