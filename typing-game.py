import pygame
import random
import time
import sys


pygame.init()
pygame.mixer.init()


pygame.mixer.music.load(r"C:\Users\nadjl\flute-oriental-japan-shakuhachi-239719.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)


unmute_sound = pygame.image.load(r"C:\Users\nadjl\sound_off.png")
mute_sound = pygame.image.load(r"C:\Users\nadjl\sound_on.png")
TAILLE_ICONE = (50, 50)
unmute_sound = pygame.transform.scale(unmute_sound, TAILLE_ICONE)
mute_sound = pygame.transform.scale(mute_sound, TAILLE_ICONE)

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SIZE = 25
WHITE = (255, 255, 255)
GREEN = (0,128,0)
background = pygame.image.load(r"C:\Users\nadjl\Downloads\backgroung.png")
pygame.display.set_caption("Fruit Ninja")
FONT = pygame.font.Font(None, SIZE)

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

# menu
main_page = True
difficulty_page = False
option_page = False
sound_active = True

# game
score = 0
combo_multiplicator = 1
last_hit_time = 0
combo_time_window = 2.0
lives = 3  
frozen = False  
freeze_end_time = 0  
freeze_duration = 3
fruits = []
bombs = []
ice_blocks = []
spawn_timer = 0
spawn_interval = 950

# define image fruit
fruit_images = [
    pygame.image.load(r"C:\Users\nadjl\apple_tran.png").convert_alpha(),
    pygame.image.load(r"C:\Users\nadjl\grape_tran.png").convert_alpha(),
    pygame.image.load(r"C:\Users\nadjl\banana_tran.png").convert_alpha(),
    pygame.image.load(r"C:\Users\nadjl\strawberry_tran.png").convert_alpha(),
]

# other images
bomb_image = pygame.image.load(r"C:\Users\nadjl\bomb_tran.png").convert_alpha()
ice_block_image = pygame.image.load(r"C:\Users\nadjl\ice_tran.png").convert_alpha()




# function of the menu
def draw_main_page():
    """MAIN PAGE"""
    pygame.draw.rect(screen, WHITE, option_rect, 5)
    pygame.draw.rect(screen, WHITE, play_rect, 5)
    pygame.draw.rect(screen, WHITE, quit_rect, 5)
    play_text = FONT.render("PLAY", True, WHITE)
    option_text = FONT.render("OPTION", True, WHITE)
    quit_text = FONT.render("QUIT", True, WHITE)
    screen.blit(option_text, (option_rect.x + 48, option_rect.y + 40))
    screen.blit(play_text, (play_rect.x + 48, play_rect.y + 40))
    screen.blit(quit_text, (quit_rect.x + 48, quit_rect.y + 40))
    draw_sound_button()

def draw_option_page():
    """OPTION PAGE"""
    pygame.draw.rect(screen, WHITE, difficulty_rect, 5)
    pygame.draw.rect(screen, WHITE, return_rect, 5)
    difficulty_text = FONT.render("DIFFICULTIES", True, WHITE)
    retour_text = FONT.render("RETURN", True, WHITE)
    screen.blit(difficulty_text, (difficulty_rect.x + 48, difficulty_rect.y + 40))
    screen.blit(retour_text, (return_rect.x + 48, return_rect.y + 40))
    draw_sound_button()

def draw_difficulties_page():
    """DIFFICULTY PAGE"""
    pygame.draw.rect(screen, WHITE, easy_rect, 5)
    pygame.draw.rect(screen, WHITE, medium_rect, 5)
    pygame.draw.rect(screen, WHITE, hard_rect, 5)
    pygame.draw.rect(screen, WHITE, return2_rect, 5)
    easy_text = FONT.render("EASY", True, WHITE)
    medium_text = FONT.render("MEDIUM", True, WHITE)
    hard_text = FONT.render("HARD", True, WHITE)
    return2_text = FONT.render("RETURN", True, WHITE)
    screen.blit(easy_text, (easy_rect.x + 48, easy_rect.y + 40))
    screen.blit(medium_text, (medium_rect.x + 48, medium_rect.y + 40))
    screen.blit(hard_text, (hard_rect.x + 48, hard_rect.y + 40))
    screen.blit(return2_text, (return2_rect.x + 48, return2_rect.y + 40))
    draw_sound_button()

def draw_sound_button():
    """FUNCTION OF THE BUTTON"""
    if sound_active:
        screen.blit(unmute_sound, (sound_rect.x, sound_rect.y))
    else:
        screen.blit(mute_sound, (sound_rect.x, sound_rect.y))

# Function of the game
def load_random_letter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return random.choice(letters)

def spawn_object():
    object_type = random.choice(["fruit","fruit", "bomb", "ice_block"])

    if object_type == "fruit":
        fruits.append({
            "pos": [random.randint(50, WIDTH - 50), HEIGHT],  
            "letter": load_random_letter(),
            "image": random.choice(fruit_images),  
            "speed": random.randint(2, 5),
            "direction": "up",  
        })
    elif object_type == "bomb":
        bombs.append({
            "pos": [random.randint(50, WIDTH - 50), HEIGHT],  
            "letter": load_random_letter(),
            "image": bomb_image,
            "speed": random.randint(2, 5),
            "direction": "up",  
        })
    elif object_type == "ice_block":
        ice_blocks.append({
            "pos": [random.randint(50, WIDTH - 50), HEIGHT], 
            "letter": load_random_letter(),
            "image": ice_block_image,
            "speed": random.randint(2, 5),
            "direction": "up",  
        })

def remove_object(letter,score, combo_multiplicator, last_hit_time, frozen, freeze_end_time):
    
    current_time = time.time()
    for fruit in fruits:
        if fruit["letter"] == letter:
          
            fruits.remove(fruit)

            if current_time - last_hit_time < combo_time_window:
                combo_multiplicator += 1
            else:
                combo_multiplicator = 1
            score += 1 * combo_multiplicator
            last_hit_time = current_time
            return

    for bomb in bombs:
        if bomb["letter"] == letter:
            print("BOOM! Game over...")
            return True  

    for ice_block in ice_blocks:
        if ice_block["letter"] == letter:
          
            print("Game paused!")
            frozen = True  
            freeze_end_time = current_time + freeze_duration  
            return False  

    return False

def draw_text(text, position):
    text_surface = FONT.render(text, True, (GREEN))
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

def draw_game_over():
    game_over_font = pygame.font.Font(None, 74) 
    game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))  
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  
    screen.blit(game_over_text, text_rect)

# main loop
clock = pygame.time.Clock()
running = True
game_over = False  

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
            if event.type == pygame.KEYDOWN:
                 pressed_letter = load_random_letter()
            if main_page:
                if option_rect.collidepoint(event.pos):
                    main_page = False
                    option_page = True
                    difficulty_page = False
                    pygame.display.set_caption("Fruit Ninja- Option")
                elif play_rect.collidepoint(event.pos):
                    main_page = False
                    game_over = False
                    score = 0
                    lives = 3
                    fruits.clear()
                    bombs.clear()
                    ice_blocks.clear()
                    pygame.display.set_caption("Fruit Ninja- Play")
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif option_page:
                if difficulty_rect.collidepoint(event.pos):
                    difficulty_page = True
                    option_page = False
                    pygame.display.set_caption("Fruit Ninja- Difficulty")
                elif return_rect.collidepoint(event.pos):
                    option_page = False
                    main_page = True
                    pygame.display.set_caption("Fruit Ninja")
            elif difficulty_page:
                if return2_rect.collidepoint(event.pos):
                    option_page = True
                    difficulty_page = False
                    pygame.display.set_caption("Fruit Ninja- Option")

    screen.blit(background, (0, 0))
    if main_page:
        draw_main_page()
    elif difficulty_page:
        draw_difficulties_page()
    elif option_page:
        draw_option_page()
    elif not main_page and not option_page and not difficulty_page:
        # game loop
        if not game_over:
            spawn_timer += clock.get_time()
            if spawn_timer >= spawn_interval:
                spawn_object()
                spawn_timer = 0

            # freeze verify
            if frozen and time.time() > freeze_end_time:
                frozen = False  

            # moving fruit
            for fruit in fruits:
                if not frozen:  
                    if fruit["direction"] == "up":
                        fruit["pos"][1] -= fruit["speed"]  
                        if fruit["pos"][1] <= 100:  
                            fruit["direction"] = "down" 
                    else:
                        fruit["pos"][1] += fruit["speed"]  

                screen.blit(fruit["image"], fruit["pos"])
                draw_text(fruit["letter"], (fruit["pos"][0] + 25, fruit["pos"][1] + 25))

                if fruit["pos"][1] > HEIGHT + 50:  
                    fruits.remove(fruit)
                    lives -= 1  # 
                    if lives <= 0:  
                        game_over = True  

            for bomb in bombs:
                if bomb["direction"] == "up":
                    bomb["pos"][1] -= bomb["speed"]  
                    if bomb["pos"][1] <= 100:  
                        bomb["direction"] = "down"  
                else:
                    bomb["pos"][1] += bomb["speed"]  

                screen.blit(bomb_image, bomb["pos"])
                draw_text(bomb["letter"], (bomb["pos"][0] + 25, bomb["pos"][1] + 25))

                if bomb["pos"][1] > HEIGHT + 50:  
                    bombs.remove(bomb)

            
            for ice_block in ice_blocks:
                if ice_block["direction"] == "up":
                    ice_block["pos"][1] -= ice_block["speed"]  
                    if ice_block["pos"][1] <= 100:  
                        ice_block["direction"] = "down"  
                else:
                    ice_block["pos"][1] += ice_block["speed"]  

                screen.blit(ice_block_image, ice_block["pos"])
                draw_text(ice_block["letter"], (ice_block["pos"][0] + 25, ice_block["pos"][1] + 25))

            
                if ice_block["pos"][1] > HEIGHT + 50:  
                    ice_blocks.remove(ice_block)

            draw_text(f"Score: {score}", (100, 20))
            draw_text(f"Combo: x{combo_multiplicator}", (350, 20))
            draw_text(f"Lives: {lives}", (600, 20))  

        if game_over:
            draw_game_over()
            pygame.display.flip()
            time.sleep(2)  # delay 
            main_page = True
            game_over = False

    pygame.display.flip()
    clock.tick(60)