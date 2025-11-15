

import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("My First Pygame Screen")


clock = pygame.time.Clock()
FPS = 60  

running = True
print("Starting Pygame window...")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

    screen.fill(SKY_BLUE)

    pygame.display.flip()


    clock.tick(FPS)


pygame.quit()
sys.exit()

print("Pygame window closed.")