import pygame
import random
import string

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Fruit Ninja")

        self.clock = pygame.time.Clock()
        self.is_paused = False
        self.pause_duration = 3000
        self.bomb_triggered = False
        self.running = True
        
        self.font = pygame.font.Font(None, 40)
        self.fruits = []
        self.spawn_fruit() 

        self.bomb_sound = pygame.mixer.Sound("bomb-explosion.mp3")
        self.freeze_sound = pygame.mixer.Sound("ice-cracking.mp3")


    def spawn_fruit(self):
        """Creates random fruits, bomb, and ice block"""
        colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0)]
        used_keys = set() 
        def get_unique_letter():
            while True:
                letter = random.choice(string.ascii_uppercase)
                if letter not in used_keys:
                    used_keys.add(letter)
                    return letter

        self.fruits = [
            {
                "pos": (random.randint(100, 700), random.randint(100, 500)),
                "color": random.choice(colors),
                "letter": get_unique_letter(),
            }
            for _ in range(3)
        ]
        self.bomb = {
            "pos": (random.randint(100, 700), random.randint(100, 500)),
            "color": (0, 0, 0),
            "letter": get_unique_letter(),
        }
        self.ice_block = {
            "pos": (random.randint(100, 700), random.randint(100, 500)),
            "color": (0, 0, 255),
            "letter": get_unique_letter(),
        }

    def freeze_game(self):
        """Pauses the game temporarily"""
        if not self.bomb_triggered:
            self.is_paused = True
            self.freeze_sound.play()
            print("Game paused!")
            pygame.time.set_timer(pygame.USEREVENT, self.pause_duration)

    def trigger_bomb(self):
        """Ends the game when the bomb touch"""
        self.bomb_triggered = True
        self.bomb_sound.play() 
        print("BOOM! Game over...")

        pygame.time.delay(2000) 
        self.running = False


    def remove_fruit(self, letter):
        """Removes a fruit or activates effects if the correct key is pressed."""
        for fruit in self.fruits:
            if fruit["letter"] == letter:
                self.fruits.remove(fruit)
                return

        if self.bomb["letter"] == letter:
            self.trigger_bomb()

        if self.ice_block["letter"] == letter:
            self.freeze_game()

    def draw_text(self, text, position):
        """Draws text at the specified position."""
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)

    def run(self):
        while self.running:
            self.screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    self.remove_fruit(pygame.key.name(event.key).upper())

                if event.type == pygame.USEREVENT:
                    self.is_paused = False
                    print("Game resumed!")

            if not self.bomb_triggered:
                if not self.is_paused:
                    for fruit in self.fruits:
                        pygame.draw.circle(self.screen, fruit["color"], fruit["pos"], 30)
                        self.draw_text(fruit["letter"], fruit["pos"])

                pygame.draw.circle(self.screen, self.bomb["color"], self.bomb["pos"], 30)
                self.draw_text(self.bomb["letter"], self.bomb["pos"])

                pygame.draw.rect(self.screen, self.ice_block["color"], (*self.ice_block["pos"], 40, 40))
                self.draw_text(self.ice_block["letter"], (self.ice_block["pos"][0] + 20, self.ice_block["pos"][1] + 20))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()