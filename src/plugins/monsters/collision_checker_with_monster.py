from plugins.monsters.monster import GroundMonster
from plugins.monsters.monsters_directions import Direction

import pygame as py

class CollisionCheckerWithMonsters:
    @classmethod
    def check_collisions_between_screen_and_monsters(cls, monsters : list[GroundMonster], screen : py.Surface) -> None:
        for monster in monsters:
            cls.check_collisions_with_screen(screen, monster)
    
    @staticmethod
    def check_collisions_with_screen(screen : py.Surface, monster : GroundMonster) -> None:
        if monster.rect.left < 0:
            monster.x = 0
            monster.direction = Direction.RIGHT
            
        elif monster.rect.right > screen.get_width():
            monster.x = screen.get_width() - monster.image.get_width()
            monster.direction = Direction.LEFT