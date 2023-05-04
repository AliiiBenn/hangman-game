import pygame as py



class DirectionTimer:
    def __init__(self, repeat_move : int) -> None:
        self.last_move = py.time.get_ticks()
        self.repeat_move = repeat_move
        
    def check(self) -> bool:
        now = py.time.get_ticks()
        if now - self.last_move > self.repeat_move:
            self.last_move = now
            return True
        return False