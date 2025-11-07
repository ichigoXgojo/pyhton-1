import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('adding images and background image')

background_image = pygame.transform.scale
pygame.image.load('BLUE LOCK.jpg').convert(),
(SCREEN_WIDTH, SCREEN_HEIGHT)

player_image = pygame.transform.scale
player_image = pygame.image.load('ISSAGI.webp').convert_alpha(), (100, 100)
player_rect = player_image.get_rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)

text = pygame.font.Font(None, 36).render('ISSAGI', True, 
                                pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_HEIGHT // 2, 50))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(player_image, player_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    game_loop()

