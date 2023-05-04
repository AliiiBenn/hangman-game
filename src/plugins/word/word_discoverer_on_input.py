import pygame as py

from plugins.word.word_handler import WordHandler
from plugins.user_input.input import TextInput
from plugins.game_state.game_state_handler import GameStateSetter, GameStateReseter, PlayingStateGetter
from plugins.game_errors.error_handler import ErrorHandler

from game import factory

class WordDiscovererOnInput:
    """Class used to discover new letters when a key is pressed based in `WordHandler` and `TextInput classes and check if the word is discovered. If the word is discovered, set the game state to win
    """
    def __init__(self, x : int, y : int) -> None:
        
        self.word_handler = WordHandler(x, y)
        self.input = TextInput()
        self.error_handler = ErrorHandler(10)
        
        GameStateReseter.reset()

    def update(self, screen : py.Surface) -> None:
        """Check if there is a new key pressed and if so discover the corresponding letter and check if the word is discovered. If the word is discovered, set the game state to win

        Args:
            screen (py.Surface): The game screen
        """
        if not PlayingStateGetter.get("play"):
            return
        
        self.word_handler.update(screen)
        self.error_handler.update(screen)
        self.input.update()
        
        if self.input.current_key:
            discovered = self.word_handler.displayer.discover_letter(self.input.current_key)
            
            is_input_null = self.input.current_key == ""
            if not is_input_null and not discovered:
                self.error_handler.decrease_remaining_error()
            self.input.current_key = ""
            
        if self.is_word_discovered():
            GameStateSetter.set("win", True)

            
    def is_word_discovered(self) -> bool:
        """Check if the word is discovered

        Returns:
            bool: True if the word is discovered, False otherwise
        """
        return self.word_handler.displayer.hidden_word == self.word_handler.word
        
        
def register():
    return factory.register("word_discoverer_on_input", WordDiscovererOnInput)
