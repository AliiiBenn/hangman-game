import pygame as py

from game import factory

class TextInput:
    def __init__(self) -> None:
        self.current_key : str = ""
    
    def update(self) -> None:
        """Update the current key pressed
        """
        self.current_key = self.get_keys()
            
    
    def get_keys(self) -> str:
        letters = [
            "a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"
        ]
        
        keys_pressed = py.event.get(py.KEYDOWN)
        
        for key in keys_pressed:
            key_unicode : str = key.unicode
            
            is_letter = key_unicode in letters
            is_key_different = not key_unicode == self.current_key
            is_key_down = key.type == py.KEYDOWN
            
            if is_key_down and is_letter and is_key_different:
                return key_unicode
            
        return self.current_key
                
                
                
            


def register():
    return factory.register("input", TextInput)