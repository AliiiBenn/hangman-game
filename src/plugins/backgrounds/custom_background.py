import pygame as py





class CustomBackground:
    def __init__(self, file_path : str) -> None:
        self.image = py.image.load(file_path)
    
    def update(self, screen : py.Surface) -> None:
        self.draw(screen)
        
    def draw(self, screen : py.Surface) -> None:
        self.image = py.transform.scale(self.image, (screen.get_width(), screen.get_height()))
        screen.blit(self.image, (0, 0))
        
        