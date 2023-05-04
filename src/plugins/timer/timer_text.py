import pygame as py
import warnings
from datetime import timedelta

from plugins.game_state.game_state_handler import PlayingStateGetter

try:
    from game import factory
except ImportError:
    warnings.warn("This plugin is not meant to be run on its own. So it may have some errors.")


class TickTimer:
    def __init__(self) -> None:
        self.start_ticks = py.time.get_ticks()
        
        
    def update(self) -> bool:
        """Update the timer and return True if a second has passed

        Returns:
            bool: whether a second has passed or not
        """
        seconds = (py.time.get_ticks() - self.start_ticks) / 1000
        
        if seconds > 1:
            self.start_ticks = py.time.get_ticks()
            return True

        return False


class TimerText:
    """Class used to display a timer on the screen
    """
    def __init__(self, x : int, y : int, font : str, size : int):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 0)
        self.font = py.font.SysFont(font, self.size)
        self.timer_count = 0
        
        self.timer = TickTimer()
        
        
    def update(self, screen : py.Surface) -> None:
        """Check if a second has passed and increase the timer if it has. Then draw the timer on the screen

        Args:
            screen (py.Surface): The game screen
        """
        if not PlayingStateGetter.get("play"):
            return
        self.increase_timer_if_second_passed()
        self.draw(screen)

    def increase_timer_if_second_passed(self) -> None:
        """Check if a second has passed and increase the timer if it has
        """
        second_passed = self.timer.update()
        if second_passed:
            self.increase_timer()
        
    def increase_timer(self) -> None:
        """Increase the timer by one
        """
        self.timer_count += 1
        
    def draw(self, screen : py.Surface) -> None:
        """Draw the timer on the screen"""
        CONVERTED_TIME = str(timedelta(seconds=self.timer_count))
        text = self.font.render(CONVERTED_TIME, True, self.color)
        screen.blit(text, (self.x, self.y))
        
        
def register():
    return factory.register("timer_text", TimerText)



