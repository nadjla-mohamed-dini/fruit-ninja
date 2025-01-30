import pygame
import sys


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r"C:\Users\nadjl\energetic-bgm-242515.mp3")

pygame.mixer.music.play(loops= -1)
pygame.mixer.music.set_volume(0.5)
unmute_sound = pygame.image.load(r"C:\Users\nadjl\unmute.png")
mute_sound = pygame.image.load(r"C:\Users\nadjl\mute.png")

TAILLE_ICONE = (50,50)
unmute_sound = pygame.transform.scale(unmute_sound, TAILLE_ICONE) 
mute_sound = pygame.transform.scale(mute_sound, TAILLE_ICONE)



# Screen dimensions and font and size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
size = 19


WHITE = (255,255,255)
background = pygame.image.load(r"C:\Users\nadjl\Downloads\backgroung.png")

pygame.display.set_caption("Fruit Ninja")
font = pygame.font.Font(None, size)

# Buttons
option_rect = pygame.Rect(300, 250, 150, 100)
play_rect = pygame.Rect(300, 125, 150, 100)
quit_rect = pygame.Rect(300, 380, 150, 100)
return_rect = pygame.Rect(300, 330, 150, 100)
sound_rect = pygame.Rect(20, 530, TAILLE_ICONE[0], TAILLE_ICONE[1])
difficulty_rect = pygame.Rect(300, 200, 200, 100)
easy_rect = pygame.Rect(300, 125, 150, 100)
medium_rect = pygame.Rect(300, 250, 150, 100)
hard_rect = pygame.Rect(300, 380, 150, 100)
return2_rect = pygame.Rect(300, 500, 150, 100)

def draw_main_page():
    """MAIN PAGE"""
    pygame.draw.rect(screen, WHITE, option_rect, 5)
    pygame.draw.rect(screen, WHITE, play_rect, 5)
    pygame.draw.rect(screen, WHITE, quit_rect, 5)
    play_text = font.render("PLAY", True, WHITE)
    option_text = font.render("OPTION", True, WHITE)
    quit_text = font.render("QUIT", True, WHITE)
    screen.blit(option_text, (option_rect.x + 48, option_rect.y + 40))
    screen.blit(play_text, (play_rect.x + 48, play_rect.y + 40))
    screen.blit(quit_text, (quit_rect.x + 48, quit_rect.y + 40))
    draw_sound_button()


def draw_option_page():
    """OPTION PAGE"""
    pygame.draw.rect(screen, WHITE, difficulty_rect, 5)
    difficulty_text = font.render("DIFFICULTIES", True, WHITE)
    screen.blit(difficulty_text, (difficulty_rect.x + 48, difficulty_rect.y + 40))
    pygame.draw.rect(screen, WHITE, return_rect, 5)
    retour_text = font.render("RETURN", True, WHITE)
    screen.blit(retour_text, (return_rect.x + 48, return_rect.y + 40))
    draw_sound_button()
    

def draw_difficulties_page():
    """DIFFICULTY PAGE"""
    pygame.draw.rect(screen,WHITE, easy_rect,5)
    pygame.draw.rect(screen,WHITE,medium_rect,5)
    pygame.draw.rect(screen,WHITE,hard_rect,5)
    pygame.draw.rect(screen, WHITE, return2_rect, 5,)
    easy_text = font.render("EASY",True,WHITE)
    medium_text= font.render("MEDIUM",True,WHITE)
    hard_text= font.render("HARD",True,WHITE)
    return2_text = font.render("RETURN", True, WHITE)
    screen.blit(easy_text,(easy_rect.x + 48, easy_rect.y + 40))
    screen.blit(medium_text,(medium_rect.x + 48, medium_rect.y + 40))
    screen.blit(hard_text, (hard_rect.x + 48, hard_rect.y + 40))
    screen.blit(return2_text, (return2_rect.x + 48, return2_rect.y + 40,))
    draw_sound_button()

def draw_sound_button():
    """FUNCTION OF THE BUTTON"""
    if sound_active:
        screen.blit(unmute_sound, (sound_rect.x, sound_rect.y))
    else:
        screen.blit(mute_sound, (sound_rect.x, sound_rect.y))

# Game variables
main_page = True
difficulty_page = False
option_page = False
previous_page = None
sound_active = True

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sound_rect.collidepoint(event.pos):
                sound_active = not sound_active
                if sound_active:
                    pygame.mixer.music.set_volume(0.5)
                else:
                    pygame.mixer.music.set_volume(0)


            if main_page:
                if option_rect.collidepoint(event.pos):
                    main_page = False
                    option_page = True
                    difficulty_page = False
                elif play_rect.collidepoint(event.pos):
                    main_page = False
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif option_page:
                if difficulty_rect.collidepoint(event.pos):
                    difficulty_page = True
                    option_page = False
                elif return_rect.collidepoint(event.pos):
                    option_page = False
                    main_page = True
            elif difficulty_page:
                if return2_rect.collidepoint(event.pos):
                    option_page = True
                difficulty_page = False

        
    screen.blit(background,(0,0))
    if main_page:
        draw_main_page()
    elif difficulty_page:
        draw_difficulties_page()
    elif option_page:
        draw_option_page()
    
    pygame.display.flip()
