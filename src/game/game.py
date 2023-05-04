from typing import Any, Final
import pygame as py
import json
import os

from game.factory import create
from game.loader import load_modules

image_path = os.path.join(os.path.dirname(__file__), '..','..', 'assets', 'backgrounds','background_grass.png')
json_path = os.path.join(os.path.dirname(__file__),'..','..','data','plugins.json')
logo_path = os.path.join(os.path.dirname(__file__),'..','..','assets','1_1.png')

BACKGROUND_LINK = py.image.load(image_path)
LOGO_LINK = py.image.load(logo_path)

class Game:
    def __init__(self, screen_width : int, screen_height : int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = py.display.set_mode((self.screen_width, self.screen_height), py.RESIZABLE)
        self.clock = py.time.Clock()
        self.FPS : Final[int] = 60
        self.background = py.transform.scale(BACKGROUND_LINK, (self.screen_width, self.screen_height))
        py.display.set_icon(LOGO_LINK)
        py.display.set_caption(str(int(self.clock.get_fps())))
        
        self.extentions : list[Any] = []
        
        
    
    def load_extentions(self) -> None:
        with open(json_path, "r") as f:
            data = json.load(f)
            
            load_modules(data["plugins"])
            
            
            self.extentions = [create(entity) for entity in data["entities"]]
            
    
    def update_background(self) -> None:
        self.screen_width, self.screen_height = py.display.get_surface().get_size()
        self.background = py.transform.scale(BACKGROUND_LINK, (self.screen_width, self.screen_height))
        self.screen.blit(self.background, (0, 0))
            
    def reset(self):
        self.extentions = []
        self.load_extentions()

    def run(self):
        run = True
        while run:
            self.clock.tick(self.FPS)
            py.display.set_caption(str(int(self.clock.get_fps())))

            
            
            self.update_background()
            
            
            for entity in self.extentions:
                entity.update(self.screen)
            
            
            py.display.flip()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    run = False
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_r:
                       self.reset()
        py.quit()
                    

            
