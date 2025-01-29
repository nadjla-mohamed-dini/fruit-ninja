import pygame
import random
import sys


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r"C:\Users\nadjl\energetic-bgm-242515.mp3")

pygame.mixer.music.play(-1)

# Screen dimensions and font and size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
size = 19

BLACK = (0, 0, 0)
WHITE = (255,255,255)
ROSE = (139,69,19)
background = pygame.image.load(r"C:\Users\nadjl\Downloads\backgroung.png")

pygame.display.set_caption("Fruit Ninja")
font = pygame.font.Font(None, size)

# Buttons
option_rect = pygame.Rect(300, 250, 150, 100)
play_rect = pygame.Rect(300, 125, 150, 100)
quit_rect = pygame.Rect(300, 380, 150, 100)
return_rect = pygame.Rect(300, 430, 150, 100)
sound_rect = pygame.Rect(300, 300, 200, 100)
difficulte_rect = pygame.Rect(300, 150, 200, 100)


def draw_main_page():
    """MAIN PAGE"""
    pygame.draw.rect(screen, WHITE, option_rect, 5)
    pygame.draw.rect(screen, WHITE, play_rect, 5)
    pygame.draw.rect(screen, WHITE, quit_rect, 5)
    jouer_text = font.render("PLAY", True, WHITE)
    option_text = font.render("OPTION", True, WHITE)
    quitter_text = font.render("QUIT", True, WHITE)
    screen.blit(option_text, (option_rect.x + 48, option_rect.y + 40))
    screen.blit(jouer_text, (play_rect.x + 48, play_rect.y + 40))
    screen.blit(quitter_text, (quit_rect.x + 48, quit_rect.y + 40))

def draw_option_page():
    """OPTION PAGE"""
    pygame.draw.rect(screen, WHITE, sound_rect, 5)
    pygame.draw.rect(screen, WHITE, difficulte_rect, 5)
    ajout_mots_text = font.render("SOUND", True, WHITE)
    difficulte_text = font.render("DIFFICULTIES", True, WHITE)
    screen.blit(ajout_mots_text, (sound_rect.x + 78, sound_rect.y + 40))
    screen.blit(difficulte_text, (difficulte_rect.x + 48, difficulte_rect.y + 40))
    pygame.draw.rect(screen, WHITE, return_rect, 5)
    retour_text = font.render("RETURN", True, WHITE)
    screen.blit(retour_text, (return_rect.x + 48, return_rect.y + 40))


# Game variables
main_page = True
in_game = False

mutes_music = False


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_page:
                if option_rect.collidepoint(event.pos):
                    main_page = False
                elif play_rect.collidepoint(event.pos):
                    main_page = False
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            else:
                if return_rect.collidepoint(event.pos):
                    main_page = True
        
    screen.blit(background,(0,0))
    if main_page:
        draw_main_page()
    else:
        draw_option_page()
    pygame.display.flip()
