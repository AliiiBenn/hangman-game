import json
import pygame as py

from plugins.game_errors.error_displayer import ErrorDisplayer
from plugins.game_state.game_state_handler import GameStateSetter, GameStateReseter, PlayingStateGetter

from game import factory

class ErrorJsonGetter:
    @staticmethod
    def get_error_count() -> int:
        with open("data/data.json", "r") as f:
            data = json.load(f)
            
        errors = data["errors"]
        
        return errors

class ErrorJsonWriter:
    
    
    @staticmethod
    def has_error_count_changed(error : int) -> bool:
        current_error = ErrorJsonGetter.get_error_count()
        if current_error != error:
            return True
        return False
    
    @classmethod
    def update_errors(cls, error : int) -> None:
        if not cls.has_error_count_changed(error):
            return
        
        with open("data/data.json", "r") as f:
            data = json.load(f)
            
        data["errors"] = error
        
        with open("data/data.json", "w") as f:
            json.dump(data, f)
            
            
class GameOverCheckerJson:
    @staticmethod
    def is_game_over() -> bool:
        with open("data/data.json", "r") as f:
            data = json.load(f)
            
        return data["errors"] <= 0
    

class GameOverChecker:
    @staticmethod
    def is_game_over(errors : int) -> bool:
        return errors <= 0
    
    
class ErrorCountSetter:
    def __init__(self, nb_error_max : int) -> None:
        self.nb_error_max = nb_error_max
        
    def decrease_remaining_error(self) -> None:
        if self.nb_error_max <= 0:
            return
        
        self.nb_error_max -= 1

class ErrorHandler:
    """Class used to display the number of remaining error, check if the game is over and decrease the number of remaining error
    """
    def __init__(self, nb_error_max : int) -> None:
        self.nb_error_max = nb_error_max
        self.error_displayer = ErrorDisplayer(nb_error_max)
        
        GameStateReseter.reset()
        
    def update(self, screen : py.Surface) -> None:
        """Set the number of remaining error, update the error displayer and check if the game is over. If the game is over, set the game state to lose

        Args:
            screen (py.Surface): The game screen
        """
        if not PlayingStateGetter.get("play"):
            return
        
        self.error_displayer.nb_error_max = self.nb_error_max
        self.error_displayer.update(screen)
        
        ErrorJsonWriter.update_errors(self.nb_error_max)
        
        if GameOverChecker.is_game_over(self.nb_error_max):
            GameStateSetter.set("lose", True)
        
    def decrease_remaining_error(self) -> None:
        """If the number of remaining error is greater than 0, decrease the number of remaining error by 1
        """
        if self.nb_error_max <= 0:
            return
        
        self.nb_error_max -= 1
        
        
        
def register():
    return factory.register("error_handler", ErrorHandler)