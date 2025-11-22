import pygame
import random
import sys

# --- Pygame Initialization and Constants ---
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Custom Events"

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

# Set up the game clock
clock = pygame.time.Clock()
FPS = 60

# --- Custom Event Definition ---
# Pygame reserves events 0 through USEREVENT. Custom events start after USEREVENT.
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

# Set a timer to automatically trigger the custom event every 3000 milliseconds (3 seconds)
pygame.time.set_timer(COLOR_CHANGE_EVENT, 3000)


# --- Sprite Class Definition ---
class SquareSprite(pygame.sprite.Sprite):
    """A simple square sprite that can change color."""
    def __init__(self, color, size, initial_pos):
        # Initialize the base class
        super().__init__()

        # Store the current and original color
        self.original_color = color
        self.color = color

        # Create a surface (image) for the sprite
        self.image = pygame.Surface([size, size])
        self.image.fill(self.color)

        # Get the rectangle object that bounds the image
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_pos
        
        # Store the size for redrawing
        self.size = size

    def update_color(self, new_color):
        """Changes the sprite's color and updates its surface."""
        self.color = new_color
        self.image.fill(self.color)

    def reset_color(self):
        """Resets the sprite back to its original color."""
        self.color = self.original_color
        self.image.fill(self.color)


# --- Sprite Instantiation ---

# 1. Create Sprite 1 (Red, position 1)
sprite1 = SquareSprite(RED, 100, (150, 250))

# 2. Create Sprite 2 (Blue, position 2)
sprite2 = SquareSprite(BLUE, 100, (550, 250))

# Create a group to hold all sprites (makes drawing and updating easier)
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# --- Utility Function for Color Change ---
def get_random_color():
    """Generates a random RGB color tuple."""
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


# --- Main Game Loop ---
running = True
print(f"Custom Event ID: {COLOR_CHANGE_EVENT}")
print("Press SPACEBAR to manually trigger the color change event.")

while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Check for the custom event
        if event.type == COLOR_CHANGE_EVENT:
            print("COLOR_CHANGE_EVENT triggered!")
            
            # Generate a new random color
            new_color = get_random_color()
            
            # Apply the new color to both sprites
            sprite1.update_color(new_color)
            sprite2.update_color(new_color)
            
        # Check for key presses to manually trigger the event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Post the custom event to the event queue
                pygame.event.post(pygame.event.Event(COLOR_CHANGE_EVENT))
            
            if event.key == pygame.K_r:
                # Reset colors manually
                sprite1.reset_color()
                sprite2.reset_color()
                print("Colors reset to original.")

    # --- Drawing ---
    screen.fill(BLACK) # Clear the screen with black

    # Draw all sprites in the group
    all_sprites.draw(screen)

    # Display instructions
    font = pygame.font.Font(None, 36)
    text = font.render("Press SPACEBAR to change colors (or wait 3 seconds!)", True, WHITE)
    reset_text = font.render("Press 'R' to reset colors.", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 50))
    screen.blit(reset_text, (SCREEN_WIDTH // 2 - reset_text.get_width() // 2, 90))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# --- Cleanup ---
pygame.quit()
sys.exit()