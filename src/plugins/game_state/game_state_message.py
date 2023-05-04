import pygame as py
import os


image_path = os.path.join(os.path.dirname(__file__), '..','..', '..','assets','endgame_image.png')
GAME_STATE_IMAGE = py.image.load(image_path)

class WindowSquareAnimation:
    def __init__(self) -> None:
        self.INCREMENT = 5
        self.gap = 10
        
        
    def is_animation_finished(self, screen : py.Surface) -> bool:
        return self.gap >= screen.get_height()
        
    def increment_if_not_finished(self, screen : py.Surface) -> None:
        if not self.is_animation_finished(screen):
            self.gap += self.INCREMENT
            
    def increase_gap(self) -> None:
        self.gap += self.INCREMENT
            
    def draw(self, screen : py.Surface) -> None:
        py.draw.rect(screen, (0, 0, 0), (0, 0, screen.get_width(), self.gap))
        
        if not self.is_animation_finished(screen):
            self.increase_gap()
            
            
class GameStateText:
    def __init__(self, test : str, font : str, size : int, color : tuple) -> None:
        self.text = test
        self.font = py.font.SysFont(font, size)
        self.color = color
        
    def create_text(self) -> py.surface.Surface:
        return self.font.render(self.text, True, self.color)
    
    def get_centered_position(self, screen : py.surface.Surface) -> tuple:
        text = self.create_text()
        
        centered_width = screen.get_width() // 2 - text.get_width() // 2
        centered_height = screen.get_height() // 2 - text.get_height() // 2
        
        centered_position = (centered_width, centered_height)
        return centered_position
    
    def draw(self, screen : py.Surface) -> None:
        text = self.create_text()
        centered_position = self.get_centered_position(screen)
        
        screen.blit(text, centered_position)
        
        

class GameStateMessage:
    """Class Used for Initherited Class to display a game state message
    """
    def __init__(self, message: str) -> None:
        self.message = message
        self.font = py.font.SysFont("Arial", 50)
        
        self.squares_animation = WindowSquareAnimation()
        self.game_state_text = GameStateText(message, "Arial", 50, (255, 255, 255))
        self.text = self.game_state_text.create_text()
        
        
    def update(self, screen : py.Surface) -> None:
        """Update the game state message

        Args:
            screen (py.Surface): The game screen
        """
        self.draw(screen)
        
    def draw(self, screen : py.Surface) -> None:
        """Draw the game state message on the screen

        Args:
            screen (py.Surface): The game screen
        """
        
        
        self.squares_animation.draw(screen)
        
        if self.squares_animation.is_animation_finished(screen):
            image_width = GAME_STATE_IMAGE.get_width()
            image_height = GAME_STATE_IMAGE.get_height()
            
            
            screen.blit(GAME_STATE_IMAGE, (screen.get_width() // 2 - image_width // 2, (screen.get_height() // 2 - image_height // 2) - 25))
            
            self.game_state_text.draw(screen)


class WonStateMessage(GameStateMessage):
    def __init__(self) -> None:
        super().__init__("Winner !!!!")        


class LostStateMessage(GameStateMessage):
    def __init__(self) -> None:
        super().__init__("Game Over")
