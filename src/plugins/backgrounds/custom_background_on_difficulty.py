import pygame as py

from plugins.backgrounds.backgrounds import CustomBackground
from plugins.word.json_word import JsonWordGetter

from game import factory

NORMAL_BACKGROUND = "assets/backgrounds/background_grass.png"
MEDIUM_BACKGROUND = "assets/backgrounds/background_cave.png"
HARD_BACKGROUND = "assets/backgrounds/background_hell.png"

MEDIUM_LETTERS = 10
HARD_LETTERS = 15


class CustomBackGroundOnDifficulty:
    def __init__(self) -> None:
        self.word = ""
        self.word_size = 0
        
        self.background = CustomBackground(NORMAL_BACKGROUND)
        
    
    def update(self, screen : py.Surface) -> None:
        if self.word == "" and self.word_size == 0:
            self.word = JsonWordGetter.get()
            self.word_size = len(self.word)
            self.background = self.get_background()
        self.background.update(screen)
        
    def get_background(self) -> CustomBackground:
        if self.word_size < MEDIUM_LETTERS:
            return CustomBackground(NORMAL_BACKGROUND)
        elif self.word_size < HARD_LETTERS:
            return CustomBackground(MEDIUM_BACKGROUND)
        else:
            return CustomBackground(HARD_BACKGROUND)
        

def register() -> None:
    return factory.register("custom_background", CustomBackGroundOnDifficulty)
