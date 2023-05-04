
from typing import Final
import pygame as py

from game import factory

BLACK : Final[tuple[int, int, int]] = (0, 0, 0)

class TopRightTextSetter:
    @staticmethod
    def set(screen : py.Surface, text : py.surface.Surface) -> tuple[int, int]:
        text_width = text.get_width()
        screen_width = screen.get_width()
        
        TOP_RIGHT_CORNER : Final[tuple[int, int]] = (screen_width - text_width, 0)
        
        return TOP_RIGHT_CORNER


class ErrorDisplayer:
    """Class To Display The Number Of Remaining Error
    """
    def __init__(self, nb_error_max : int) -> None:
        self.nb_error_max = nb_error_max

        self.font = py.font.SysFont("Arial", 24)

    def update(self, screen : py.Surface) -> None:
        """Update the error displayer

        Args:
            screen (py.Surface): The game screen
        """
        self.draw(screen)

    def draw(self, screen : py.Surface) -> None:
        """Draw the error count in the top right corner

        Args:
            screen (py.Surface): The game screen
        """
        text = self.font.render(str(self.nb_error_max), True, BLACK)
        
        TOP_RIGHT_CORNER = TopRightTextSetter.set(screen, text)
        
        screen.blit(text, TOP_RIGHT_CORNER)



def register():
    return factory.register("error_displayer", ErrorDisplayer)