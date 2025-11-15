import pygame
import random   

# Initialize Pygame
pygame.init()

SPRIETE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
RED = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

YELLOW = pygame.Color('yellow')
GREEN = pygame.Color('green')   
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class MovingSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)

        boundary_hit = False
        if self.rect.left < 0 or self.rect.right > 800:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        
            if boundary_hit:
                pygame.event.post(pygame.event.Event(SPRIETE_COLOR_CHANGE_EVENT))
                pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
        
def change_color(self):
    bg_colors = [BLUE, RED, DARKBLUE]
    # Add logic to change the sprite color here

def change_background_color(self):
    global background_color
    bg_colors = [BLUE, RED, DARKBLUE]
    # Add logic to change the background color here

all_spriteslist = pygame.sprite.Group()

sp1 = MovingSprite(WHITE, 20, 30)

sp1.rect.x = random.randint(0, 400)
sp1.rect.y = random.randint(0, 370)

all_spriteslist.add(sp1)

screen = pygame.display.set_mode([800, 600])

pygame.display.set_caption('colorful bounce')

background_color = BLUE

screen.fill(background_color)

exit = False

clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRIETE_COLOR_CHANGE_EVENT:
            change_color(sp1)
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_spriteslist.update()

    screen.fill(background_color)

    all_spriteslist.draw(screen)

    pygame.display.flip()

    clock.tick(60)

all_spriteslist.update()

screen.fill(background_color)

all_spriteslist.draw(screen)

clock.tick(60)


pygame.quit()           