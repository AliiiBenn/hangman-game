import pygame as py

from game import factory


class CustomMouse:
    def __init__(self) -> None:
        self.image = py.image.load("assets/mouse.png")
        self.rect = self.image.get_rect()
        
        
    def update(self, screen : py.Surface) -> None:
        py.mouse.set_visible(False)
        self.rect.center = py.mouse.get_pos()
        self.draw(screen)    
    
    def draw(self, screen : py.Surface) -> None:
        screen.blit(self.image, self.rect)
        
        
def register() -> None:
    factory.register("mouse", CustomMouse)
