import json
import pygame as py
import os.path

DATA_FILE = os.path.join(os.path.dirname(__file__), '..','..', '..','data','data.json') 

class GameStateSetter:
    @staticmethod
    def set(game_state_type : str, new_state : bool) -> None:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        data[game_state_type] = new_state
        
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
            
            
class GameStateReseter:
    @staticmethod
    def reset() -> None:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        data["lose"] = False
        data["win"] = False
        
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
            
            
class GameStateGetter:
    @staticmethod
    def get(game_state_type : str) -> bool:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        return data[game_state_type]
    
    
class PlayingStateGetter:
    @staticmethod
    def get(type : str) -> bool:
        """Get the playing state for pause or play
        Args:
            type (str): The type of playing state to get
        Returns:
            bool: The playing state
        """
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        return data[type]
    
    
class PlayingStateSetter:
    @staticmethod
    def set(playing_state_type : str, new_state : bool) -> None:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        data[playing_state_type] = new_state
        
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
            
    
class PlayingStateReseter:
    @staticmethod
    def reset() -> None:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        data["pause"] = False
        data["play"] = False
        
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
    
    
            
            

        
