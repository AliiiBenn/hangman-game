import pygame as py
from pygame import mixer
import os.path
from enum import Enum

from plugins.game_state.game_state_handler import PlayingStateGetter
from plugins.word.json_word import JsonWordGetter

from game import factory


BACKGROUND_MUSIC = os.path.join(os.path.dirname(__file__),'..','..', '..','assets','sounds','musique_fond.mp3')
WIND = os.path.join(os.path.dirname(__file__),'..','..', '..','assets','sounds','vent.mp3')
BIRDS = os.path.join(os.path.dirname(__file__),'..','..', '..','assets','sounds','oiseaux.mp3')

MEDIUM_MUSIC = os.path.join(os.path.dirname(__file__),'..','..', '..','assets','sounds','medium_background_music.mp3')
HARD_MUSIC = os.path.join(os.path.dirname(__file__),'..','..', '..','assets','sounds','hard_background_music.mp3')


class WordDifficulty(Enum):
    EASY = 5
    MEDIUM = 10
    HARD = 15

class BackgroundMusic:
    def __init__(self, volume : float) -> None:
        self.volume = volume
        
        self.playing_music = False
        self.word = JsonWordGetter.get()
        self.word_length = len(self.word)
        
    
    def update(self, screen : py.Surface) -> None:
        if not PlayingStateGetter.get("play"):
            return
        
        if not self.playing_music:
            self.select_music()
            self.playing_music = True
            
    def select_music(self) -> None:
        if self.word_length <= WordDifficulty.EASY.value:
            mixer.Channel(1).play(mixer.Sound(BACKGROUND_MUSIC), -1)
            mixer.Channel(1).set_volume(self.volume)
        elif self.word_length <= WordDifficulty.MEDIUM.value:
            mixer.Channel(2).play(mixer.Sound(MEDIUM_MUSIC), -1)
            mixer.Channel(2).set_volume(self.volume)
        else:
            mixer.Channel(3).play(mixer.Sound(HARD_MUSIC), -1)
            mixer.Channel(3).set_volume(self.volume)
        
    def play(self) -> None:
        # print("Playing music")
        pass
        
        
def register() -> None:
    factory.register("BackgroundMusic", BackgroundMusic)
