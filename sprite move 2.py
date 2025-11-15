import pygame
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Two Sprites with Movement")

# Define colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


sprite1_size = 50
sprite1_rect = pygame.Rect(50, 50, sprite1_size, sprite1_size)
SPRITE1_SPEED = 5


sprite2_width = 100
sprite2_height = 70
sprite2_rect = pygame.Rect(SCREEN_WIDTH - sprite2_width - 50, SCREEN_HEIGHT - sprite2_height - 50, sprite2_width, sprite2_height)


clock = pygame.time.Clock()
FPS = 60


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    dx = 0
    dy = 0

    if keys[pygame.K_LEFT]:
        dx = -SPRITE1_SPEED
    if keys[pygame.K_RIGHT]:
        dx = SPRITE1_SPEED
    if keys[pygame.K_UP]:
        dy = -SPRITE1_SPEED
    if keys[pygame.K_DOWN]:
        dy = SPRITE1_SPEED

    sprite1_rect.x += dx
    sprite1_rect.y += dy
    

    if sprite1_rect.left < 0:
        sprite1_rect.left = 0
    if sprite1_rect.right > SCREEN_WIDTH:
        sprite1_rect.right = SCREEN_WIDTH

    if sprite1_rect.top < 0:
        sprite1_rect.top = 0
    if sprite1_rect.bottom > SCREEN_HEIGHT:
        sprite1_rect.bottom = SCREEN_HEIGHT


    screen.fill(BLACK)
    
    pygame.draw.rect(screen, RED, sprite1_rect)
    
    pygame.draw.rect(screen, BLUE, sprite2_rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()