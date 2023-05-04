import pygame as py

from plugins.backgrounds.backgrounds import CustomBackground
from plugins.word.json_word import JsonWordGetter

from game import factory



NORMAL_BACKGROUND = "assets/backgrounds/background_grass.png"
MEDIUM_BACKGROUND = "assets/backgrounds/background_cave.png"
HARD_BACKGROUND = "assets/backgrounds/background_hell.png"

MEDIUM_LETTERS = 10
HARD_LETTERS = 15


from abc import ABC, abstractmethod

class BackgroundStrategy(ABC):
    @abstractmethod
    def get_background(self) -> CustomBackground:
        pass
    
    
class NormalBackgroundStrategy(BackgroundStrategy):
    def get_background(self) -> CustomBackground:
        return CustomBackground(NORMAL_BACKGROUND)
    
    
class MediumBackgroundStrategy(BackgroundStrategy):
    def get_background(self) -> CustomBackground:
        return CustomBackground(MEDIUM_BACKGROUND)
    
    
class HardBackgroundStrategy(BackgroundStrategy):
    def get_background(self) -> CustomBackground:
        return CustomBackground(HARD_BACKGROUND)


class BackgroundStrategyFactory:
    @staticmethod
    def create(word_size : int) -> BackgroundStrategy:
        if word_size < MEDIUM_LETTERS:
            return NormalBackgroundStrategy()
        elif word_size < HARD_LETTERS:
            return MediumBackgroundStrategy()
        else:
            return HardBackgroundStrategy()
    
    
class BackgroundSetterOnDifficulty:
    def __init__(self) -> None:
        self.word_size = 0
        self.background = None
        
        
    def update(self, screen : py.Surface) -> None:
        if self.word_size == 0:
            self.word_size = len(JsonWordGetter.get())
        if self.background is None:
            self.background = self.set_background()
        return self.background.update(screen)
        
    def set_background(self) -> CustomBackground:
        return BackgroundStrategyFactory.create(self.word_size).get_background()
    
        

def register() -> None:
    return factory.register("custom_background", BackgroundSetterOnDifficulty)
