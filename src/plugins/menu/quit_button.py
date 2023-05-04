from plugins.menu.button import Button
from plugins.game_state.game_state_handler import PlayingStateSetter, PlayingStateReseter

import pygame as py
import sys

from game import factory


class QuitButton(Button):
    def __init__(self, margin : int):
        super().__init__(margin, "quit_button")
        PlayingStateReseter.reset()
        
    def update(self, screen: py.Surface) -> None:
        return super().update(screen)
    
    def on_press(self) -> None:
        mouse_pos = py.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos) and py.mouse.get_pressed()[0]:
            sys.exit()
            
            
            
def register() -> None:
    return factory.register("quit_button", QuitButton)