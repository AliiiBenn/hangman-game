from plugins.monsters.monsters_creator import GroundMonstersCreator
from plugins.monsters.monsters_remover_on_error import GroundMonsterRemoverOnError
from plugins.monsters.collision_checker_with_monster import CollisionCheckerWithMonsters

from plugins.game_state.game_state_handler import GameStateGetter, PlayingStateGetter

import pygame as py


from game import factory


class GroundMonstersHandler:
    def __init__(self, count : int) -> None:
        self.count = count
        
        self.monsters_creator = GroundMonstersCreator(count)
        self.monsters_remover = GroundMonsterRemoverOnError(self.monsters_creator.monsters)
        
    def update(self, screen : py.Surface) -> None:
        if GameStateGetter.get("lose") or GameStateGetter.get("win") or not PlayingStateGetter.get("play"):
            return
        
        self.monsters_remover.update(screen)
        
        
        if not self.monsters_creator.monsters:
            self.monsters_creator.add_monsters(screen, self.count)
            self.monsters_remover.monsters_count = len(self.monsters_creator.monsters)
            
        CollisionCheckerWithMonsters.check_collisions_between_screen_and_monsters(self.monsters_creator.monsters, screen)
        for monster in self.monsters_creator.monsters:
            monster.update(screen)
            
            
            
def register() -> None:
    factory.register("ground_monsters_handler", GroundMonstersHandler)