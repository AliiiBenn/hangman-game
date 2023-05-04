from typing import Optional, Union
import pygame as py

from plugins.game_state.game_state_handler import GameStateGetter
from plugins.game_state.game_state_message import WonStateMessage, LostStateMessage

from game import factory


class DisplayTextOnGameState:
    """Class used to display a message when the game is won or lost
    """
    def __init__(self) -> None:
        self.current_game_state_message : Optional[Union[WonStateMessage, LostStateMessage]] = None
        
    def set_game_state_message(self) -> None:
        """Set the current game state message
        """
        has_won = GameStateGetter.get("win")
        has_lost = GameStateGetter.get("lose")
        
        if has_won:
            self.current_game_state_message = WonStateMessage()
        elif has_lost:
            self.current_game_state_message = LostStateMessage()
    
    def update(self, screen : py.Surface) -> None:
        """Check if the game is won or lost and display the corresponding message

        Args:
            screen (py.Surface): The game screen
        """
        
        if self.current_game_state_message is None:
            self.set_game_state_message()
        else:
            self.current_game_state_message.update(screen)
            
        
            
            
def register():
    return factory.register("display_text_on_game_state", DisplayTextOnGameState)