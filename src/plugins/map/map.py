import pygame as py

import os.path
from game import factory

from plugins.game_state.game_state_handler import GameStateGetter, PlayingStateGetter
from plugins.word.json_word import JsonWordGetter

from enum import Enum

class MapBlockCreator:
    def __init__(self, width : int, height : int, x : int, y : int, file_path : str) -> None:
        self.width = width
        self.height = height 
        self.x = x
        self.y = y
        
        self.image_path = os.path.join(os.path.dirname(__file__),'..','..', '..',file_path)
        self.image = py.image.load(self.image_path)
        self.image = py.transform.scale(self.image, (self.width, self.height))
        self.rect = py.Rect(self.x, self.y, self.width, self.height)

    def update(self, screen : py.Surface) -> None:
        self.draw(screen)

    def draw(self, screen : py.Surface) -> None:
        self.image = py.transform.scale(self.image, (self.width, self.height))
        self.rect = py.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.image, self.rect)


class ScreenLineBlockCreator:
    def __init__(self, block_count : int, up_y : int, block_file_path : str) -> None:
        self.block_count = block_count
        self.up_y = up_y
        self.block_file_path = block_file_path

        self.blocks : list[MapBlockCreator] = []

    def update(self, screen : py.Surface) -> None:
        if GameStateGetter.get("win") or GameStateGetter.get("lose") or not PlayingStateGetter.get("play"):
            return
        if not self.blocks:
            self.create_blocks(screen)
        self.draw_blocks(screen)

    def create_blocks(self, screen : py.Surface) -> None:
        for i in range(self.block_count + 1):
            new_block = MapBlockCreator(screen.get_width() // self.block_count,
                                        64,
                                        i*(screen.get_width() // self.block_count),
                                        screen.get_height() - 64,
                                        self.block_file_path)
            self.blocks.append(new_block)

    def draw_blocks(self, screen : py.Surface) -> None:
        for i, block in enumerate(self.blocks):
            block.width = screen.get_width() // self.block_count 
            block.x = i*(screen.get_width() // self.block_count)
            block.y = screen.get_height() - self.up_y
            block.draw(screen)



class CustomMap:
    def __init__(self, block_count : int, dirt_image_path : str, ground_image_path : str) -> None:
        self.block_count = block_count
        self.dirt_image_path = dirt_image_path
        self.ground_image_path = ground_image_path

        self.blocks_lines : list[ScreenLineBlockCreator] = []
        
    def update(self, screen : py.Surface) -> None:
        if len(self.blocks_lines) == 0:
            self.set_block_lines()
        
        for lines in self.blocks_lines:
            lines.update(screen)
            
    def set_block_lines(self) -> None:
        self.blocks_lines.append(ScreenLineBlockCreator(self.block_count, 64, self.dirt_image_path))
        self.blocks_lines.append(ScreenLineBlockCreator(self.block_count, 128, self.ground_image_path))
        
        
class Maps(Enum):
    NORMAL = CustomMap(15, "assets/map/normal_dirt.png", "assets/map/normal_grass.png")
    MEDIUM = CustomMap(15, "assets/map/medium_dirt.png", "assets/map/medium_grass.png")
    HARD = CustomMap(15, "assets/map/hard_dirt.png", "assets/map/hard_grass.png")


class MapDifficulty(Enum):
    NORMAL = 5
    MEDIUM = 10
    HARD = 15


class Map:
    def __init__(self) -> None:
        self.word = JsonWordGetter.get()
        self.word_length = len(self.word)
        
        self.map = self.set_map()
        
    
    def update(self, screen : py.Surface) -> None:
        self.map.update(screen)
        
    def set_map(self) -> CustomMap:
        if self.word_length < MapDifficulty.MEDIUM.value:
            return Maps.NORMAL.value
        elif self.word_length < MapDifficulty.HARD.value:
            return Maps.MEDIUM.value
        else:
            return Maps.HARD.value
        

def register():
    return factory.register("map", Map)
