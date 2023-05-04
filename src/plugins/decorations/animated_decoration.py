import pygame as py

from game import factory


class AnimatedDecoration:
    def __init__(self, x : int, y : int, file_path: str) -> None:
        self.x = x
        self.y = y
        self.file_path = file_path
        
        
        self.image = py.image.load(self.file_path)
        self.image = py.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        
    def update(self, screen : py.Surface) -> None:
        self.draw(screen)
        
    def draw(self, screen : py.Surface) -> None:
        screen.blit(self.image, (self.x, self.y)) 
        
        
def register() -> None:
    factory.register("animated_decoration", AnimatedDecoration)