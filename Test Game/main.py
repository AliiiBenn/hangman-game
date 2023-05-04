import pygame
import time
import random
import numpy as np

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Letters")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
FONT_SIZE = 36
font = pygame.font.SysFont(None, FONT_SIZE)

#Define class for the Hidden word
class HiddenWord:
    def __init__(self, filename):
        self.word = self.get_random_word(filename)
        self.display_word = ["_" for _ in range(len(self.word))]
        self.position = np.array([WIDTH/2 - FONT_SIZE*len(self.word)/2, HEIGHT/2])
        self.discovered_letters = []

    def get_random_word(self, filename):
        with open(filename, 'r') as f:
            words = f.readlines()
        return random.choice(words).strip().upper()

    def update(self ):
        pass
    def draw(self):
        displayed_text = ""
        for i in range(len(self.word)):
            if self.word[i] in self.discovered_letters:
                displayed_text += self.word[i] + " "
            else:
                displayed_text += self.display_word[i] + " "
        text = font.render(displayed_text, True, WHITE)
        screen.blit(text, ((WIDTH - text.get_width())/2, (HEIGHT - FONT_SIZE)/2))

    def reveal_letter(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.display_word[i] = letter
        print(letter)
        print(self.word)
        print(self.display_word)

hidden_word = HiddenWord("liste_mots.txt")


# Define class for characters
class Character:
    def __init__(self, letter):
        self.letter = letter
        self.position = np.array([random.randint(0, WIDTH - FONT_SIZE), -FONT_SIZE])
        self.velocity = np.array([0, 3])

    def update(self):
        self.position += self.velocity

    def draw(self):
        text = font.render(self.letter, True, WHITE)
        screen.blit(text, tuple(self.position))

    def get_rect(self):
        text = font.render(self.letter, True, WHITE)
        return pygame.Rect(*self.position, text.get_width(), text.get_height())

# Define class for player
class Player:
    def __init__(self):
        self.position = np.array([400,400])
        self.velocity = np.array([0, 0])
        self.is_dashing = False
        self.dash_timer = 0.0
        self.dash_duration = 0.5
        self.sprite_sheet = pygame.image.load('./player/bear_walk.png')
        self.frame_width = 40 
        self.frame_height = 40
        self.num_frames =6 
        self.animation_speed = 0.1
        self.animation_index = 0.0
        self.current_frame = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity[0] = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity[0] = 5
        else:
            self.velocity[0] = 0
        
        if keys[pygame.K_LCTRL]:
            self.is_dashing = True 

        if self.is_dashing:
            self.velocity *= 3

            self.dash_timer = max(0.0, self.dash_timer - 0.1)
            if self.dash_timer == 0.0:
                self.is_dashing = False

        self.position += self.velocity

        if self.position[0] < 0:
            self.position[0] = 0
        elif self.position[0] > WIDTH - FONT_SIZE:
            self.position[0] = WIDTH - FONT_SIZE
        speed = np.linalg.norm(self.velocity)
        if speed > 0:

            self.animation_index += self.animation_speed
            if self.animation_index >= 1.0:
                self.animation_index = 0

            direction = self.velocity / speed
            self.current_frame = int(self.animation_index * self.num_frames)
            if self.current_frame > self.num_frames:
                self.current_frame += 0
        else:
            self.current_frame = 0

    def draw(self):
        rotated_image = self.sprite_sheet.copy()
        angle = -np.degrees(np.arctan2(self.velocity[1], self.velocity[0]))
        rotated_image = pygame.transform.rotate(rotated_image, angle)
        frame_x = self.current_frame * self.frame_width 
        frame_y = 0
        frame_rect = pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height)
        screen.blit(rotated_image, self.position, frame_rect)

    def get_rect(self):
        return pygame.Rect(*self.position, FONT_SIZE, FONT_SIZE)

# Initialize game objects
characters = []
player = Player()

SPAWN_TIME = 1000
spawn_timer = SPAWN_TIME

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    # Update game objects
    player.update()
    hidden_word.update()

    spawn_timer -= pygame.time.get_ticks() % SPAWN_TIME
    if spawn_timer <= 0:
        letter = chr(random.randint(65, 90))
        characters.append(Character(letter))
        spawn_timer = SPAWN_TIME 

    for character in characters:
        character.update()

        # Check for collision with player
        if character.get_rect().colliderect(player.get_rect()):
            hidden_word.reveal_letter(character.letter)
            characters.remove(character)
            print(character.letter)

        # Remove characters that have fallen off the screen
        if character.position[1] > HEIGHT:
            characters.remove(character)



    # Draw screen
    screen.fill(BLACK)
    player.draw()
    hidden_word.draw()
    for character in characters:
        character.draw()
    pygame.display.flip()

    if "_" not in hidden_word.display_word:
        time.sleep(5)
        hidden_word = HiddenWord("liste_mots.txt")

    # Set frame rate
    pygame.time.delay(16)

# Quit game
pygame.quit()

