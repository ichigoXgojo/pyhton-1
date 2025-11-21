import pygame

import random

# Constants for easier adjustments

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

MOVEMENT_SPEED = 5

FONT_SIZE = 72

# Initialize Pygame

pygame.init()

# Load and transform the background image

background_image = pygame.transform.scale(pygame.image.load("nate-ryman-outdoorpracticefield3.jpg"),

(SCREEN_WIDTH, SCREEN_HEIGHT))

# Load font once at the beginning

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect [0, 0, width, height])
        self.rect = self.image.get_rect()
    
    def move(self, x_change, y_change):
        
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
    
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

Sprite1 = Sprite(pygame.Color('black'), 20, 50)
Sprite1.rect.x, Sprite1.rect.y = random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT = Sprite1.rect.height)
all_sprites.add(Sprite1)

Sprite2 = Sprite(pygame.Color('red'), 20, 50)       
Sprite2.rect.x, Sprite2.rect.y = random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - Sprite2.rect.height)
all_sprites.add(Sprite2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED  
    Sprite1.move(x_change, y_change)
    
if won:
    win_text = font.render("You Win!", True, pygame.Color('green'))
    screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2, (SCREEN_HEIGHT - win_text.get_height()) // 2))

pygame.display.flip()
clock.tick(60)
pygame.quit()