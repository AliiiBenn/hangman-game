from plugins.monsters.monster import GroundMonster
from plugins.game_errors.error_handler import ErrorJsonGetter

import pygame as py



class GroundMonsterRemoverOnError:
    def __init__(self, monsters : list[GroundMonster]) -> None:
        self.monsters = monsters
        self.monsters_count = len(self.monsters)
        
    def update(self, screen : py.Surface) -> None:
        if self.has_error_changed():
            monster_to_kill = self.pick_non_dead_monster()
            if monster_to_kill:
                self.kill_monster(monster_to_kill)
    
    def has_error_changed(self) -> bool:
        if ErrorJsonGetter.get_error_count() < self.monsters_count:
            return True
        return False
    
    def pick_non_dead_monster(self) -> GroundMonster:
        for monster in self.monsters:
            if not monster.dead:
                return monster
        return None
    
    def kill_monster(self, monster : GroundMonster) -> None:
        monster.dead = True
        self.monsters_count -= 1