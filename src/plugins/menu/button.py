import pygame as py


from plugins.game_state.game_state_handler import PlayingStateGetter


class Button:
    def __init__(self, margin : int, file_name : str) -> None:
        self.margin = margin
        self.image = py.image.load(f"assets\\{file_name}.png")
        self.rect = self.image.get_rect()
        
    
    def update(self, screen : py.Surface) -> None:
        if PlayingStateGetter.get("play"):
            return
        self.rect.x = screen.get_width() // 2 - self.image.get_width() // 2
        self.rect.y = screen.get_height() // 2 - self.image.get_height() // 2 + self.margin
        self.draw(screen)
        self.on_press()
        
    def on_press(self) -> None:
        raise NotImplementedError("on_press() is not implemented it must be implemented in the child class")
        
    def draw(self, screen : py.Surface) -> None:
        screen.blit(self.image, self.rect)
        
        







        
        

        

        

