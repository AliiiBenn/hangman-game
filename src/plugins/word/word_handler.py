import pygame as py

from plugins.word.word_displayer import WordDisplayer
from plugins.word.random_word_loader import load_random_word

from game import factory

from plugins.word.json_word import JsonWordSetter
    
    


class WordHandler:
    """Class used to load a random word and display it
    """
    def __init__(self, x : int, y : int) -> None:
        self.word = load_random_word("texts\\liste_mots.txt")
        self.displayer = WordDisplayer(self.word, x, y)
        JsonWordSetter.set(self.word)
        
        print(self.word)

    def update(self, screen : py.Surface) -> None:
        """Draw the word on the screen

        Args:
            screen (py.Surface): The game screen
        """
        self.displayer.draw(screen)
    


def register():
    return factory.register("word_handler", WordHandler)