

from plugins.backgrounds.custom_background import CustomBackground
from abc import ABC, abstractmethod

MEDIUM_LETTERS = 10
HARD_LETTERS = 15

NORMAL_BACKGROUND = "assets/backgrounds/background_grass.png"
MEDIUM_BACKGROUND = "assets/backgrounds/background_cave.png"
HARD_BACKGROUND = "assets/backgrounds/background_hell.png"



class BackgroundStrategy(ABC):
    """Abstract class for background strategies based on the difficulty of the word"""
    @abstractmethod
    def get_background(self) -> CustomBackground:
        pass
    
    
class NormalBackgroundStrategy(BackgroundStrategy):
    """Background strategy for words with less than 10 letters"""
    def get_background(self) -> CustomBackground:
        return CustomBackground(NORMAL_BACKGROUND)
    
    
class MediumBackgroundStrategy(BackgroundStrategy):
    """Background strategy for words with less than 15 letters"""
    def get_background(self) -> CustomBackground:
        return CustomBackground(MEDIUM_BACKGROUND)
    
    
class HardBackgroundStrategy(BackgroundStrategy):
    """Background strategy for words with more than 15 letters"""
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