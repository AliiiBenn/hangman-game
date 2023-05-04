from typing import Final
import pygame as py

from game import factory

BACKGROUND_WORD_IMAGE : Final = py.image.load("assets\\empty_text_block.png")


class BackgroundWordImage:
    def __init__(self) -> None:
        self.image = BACKGROUND_WORD_IMAGE
        self.rect = self.image.get_rect()

    def update(self, screen : py.Surface) -> None:
        self.draw(screen)

    def draw(self, screen : py.Surface) -> None:
        self.rect.x = screen.get_width() // 2 - self.image.get_width() // 2
        self.rect.y = screen.get_height() // 2 - self.image.get_height() // 2
        
        
        screen.blit(self.image, self.rect)

class HiddenWordSetter:
    @staticmethod
    def set(word_to_hide : str) -> str:
        hidden_word = ["_" for _ in range(len(word_to_hide))]
        hidden_word[0] = word_to_hide[0]
        hidden_word[-1] = word_to_hide[-1]
        
        for i, letter in enumerate(word_to_hide):
            if letter == hidden_word[0]:
                hidden_word[i] = letter
            elif letter == hidden_word[-1]:
                hidden_word[i] = letter


        return ''.join(hidden_word)


class WordDisplayer:
    """Class used to display the word to guess on the screen
    """
    def __init__(self, word : str, x : int, y : int) -> None:
        self.word = word
        self.pos = (x, y)
        self.hidden_word = HiddenWordSetter.set(self.word)
        
        self.background_word_image = BackgroundWordImage()

        self.word_size = 40
        self.font = py.font.SysFont("Arial", self.word_size)

    def draw(self, screen : py.Surface) -> None:
        """Draw the word to guess on the center of the screen

        Args:
            screen (py.Surface): The game screen
        """
        text = self.font.render(self.hidden_word, True, (0, 0, 0))
        width = screen.get_width() // 2 - text.get_width() // 2
        height = screen.get_height() // 2 - text.get_height() // 2
        
        # self.word_size = screen.get_width() // 30
        self.font = py.font.SysFont("Arial", self.word_size)
        
        self.background_word_image.update(screen)
        
        screen.blit(text, (width, height))
    
    def discover_letter(self, new_letter : str) -> bool:
        """Discover the letter in the hidden word if it is in the word to guess

        Args:
            new_letter (str): The new letter to discover
        """
        new_hidden_word = list(self.hidden_word)
        
        discovered = False
        
        for i, letter in enumerate(self.word):
            if letter == new_letter:
                new_hidden_word[i] = letter
                discovered = True
                
        self.hidden_word = ''.join(new_hidden_word)
        
        return discovered
                


def register():
    return factory.register("word_displayer", WordDisplayer)



    