import pygame as py
from typing import Protocol



class TextCreator(Protocol):
    def update(self, screen : py.Surface) -> None:
        ...
        
        
