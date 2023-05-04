import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the clock
clock = pygame.time.Clock()

# Load the word list
with open("words.txt") as f:
    words = f.readlines()
    # Choose a random word from the list
    word = random.choice(words).strip()

# Set up the font
font = pygame.font.Font(None, 48)

class HiddenWord:
    def __init__(self, word):
        self.word = word
        self.hidden = ["_" for i in range(len(word) - 2)]
        self.hidden.insert(0, word[0])
        self.hidden.append(word[-1])
        self.text = font.render(" ".join(self.hidden), True, (255, 255, 255))

    def update(self, letter):
        for i in range(1, len(self.word) - 1):
            if self.word[i] == letter:
                self.hidden[i] = letter
        self.text = font.render(" ".join(self.hidden), True, (255, 255, 255))

    def is_completed(self):
        return '_' not in self.hidden
    
    def new_word(self):
        with open("words.txt") as f:
            words = f.readlines()
            # Choose a random word from the list
            self.word = random.choice(words).strip()
        self.hidden = ["_" for i in range(len(self.word) - 2)]
        self.hidden.insert(0, self.word[0])
        self.hidden.append(self.word[-1])
        self.text = font.render(" ".join(self.hidden), True, (255, 255, 255))



class Letter(pygame.sprite.Sprite):
    def __init__(self, letter, position):
        super().__init__()
        self.image = font.render(letter, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.letter = letter

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5

    def update(self):
        self.rect.move_ip(self.velocity.x, self.velocity.y)

        # Keep the player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

# Create the hidden word object
hidden_word = HiddenWord(word)

# Create the letters and add them to a group
letter_group = pygame.sprite.Group()
def spawn_letters(word):
    for i in range(len(word)):
        if i == 0 or i == len(word) - 1:
            continue
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        letter = Letter(word[i], (x, y))
        letter_group.add(letter)

# Create the player object
player = Player((screen_width / 2, screen_height / 2))
spawn_letters(word)
# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.velocity.x = -player.speed
            elif event.key == pygame.K_RIGHT:
                player.velocity.x = player.speed
            elif event.key == pygame.K_UP:
                player.velocity.y = -player.speed
            elif event.key == pygame.K_DOWN:
                player.velocity.y = player.speed
    # Update the player
    player.update()

    # Check for collisions between the player and letters
    letter_collisions = pygame.sprite.spritecollide(player, letter_group, True)
    for letter in letter_collisions:
        hidden_word.update(letter.letter)

    if hidden_word.is_completed():
        hidden_word.new_word()
        spawn_letters(hidden_word.word)

    # Draw the background and hidden word
    screen.fill((0, 0, 0))
    screen.blit(hidden_word.text, (screen_width / 2 - hidden_word.text.get_width() / 2,
                                   screen_height / 2 - hidden_word.text.get_height() / 2))

    # Draw the letters and player
    letter_group.draw(screen)
    screen.blit(player.image, player.rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()


