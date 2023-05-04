import pygame as py

from plugins.backgrounds.custom_background import CustomBackground
from plugins.word.json_word import JsonWordGetter

from game import factory
from .background_strategies import BackgroundStrategyFactory


class BackgroundSetterOnDifficulty:
    def __init__(self) -> None:
        self.word_size = 0
        self.background = None
        
        
    def update(self, screen : py.Surface) -> None:
        WORD_NOT_SET = self.word_size == 0
        
        if WORD_NOT_SET:
            self.word_size = len(JsonWordGetter.get())
        if self.background is None:
            self.background = self.set_background()
        return self.background.update(screen)
        
    def set_background(self) -> CustomBackground:
        return BackgroundStrategyFactory.create(self.word_size).get_background()


def register() -> None:
    return factory.register("custom_background", BackgroundSetterOnDifficulty)
