import pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Elements Example")
clock = pygame.time.Clock()

def draw_rectangle():
    # Draw a blue rectangle
    pygame.draw.rect(screen, BLUE, [50, 50, 150, 100])

def display_text():
    # Set up font
    font = pygame.font.Font(None, 36)
    # Render text
    text = font.render("Hello, Pygame!", True, GREEN)
    # Get text rectangle for positioning
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    # Blit (draw) the text onto the screen
    screen.blit(text, text_rect)

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing
    screen.fill(BLACK)  # Fill the screen with black to clear previous frame
    draw_rectangle()
    display_text()

    # Update the display