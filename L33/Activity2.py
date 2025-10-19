import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

display_surf = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding the background image')

background_image = pygame.transform.scale(pygame.image.load('Green_hill.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

sonic_image = pygame.transform.scale(pygame.image.load('Classic_Sonic.png').convert_alpha(), (200,200))
penguin_rect = sonic_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT // 2-30))

text = pygame.font.Font(None, 36).render('Sonic in Green Hill!', True, pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        display_surf.blit(background_image, (0,0))
        display_surf.blit(sonic_image, penguin_rect)
        display_surf.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':

    game_loop()        