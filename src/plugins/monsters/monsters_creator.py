from plugins.monsters.monster import GroundMonster

from plugins.entity_animator.animation_data import EntityAnimationData

from plugins.word.json_word import JsonWordGetter

import pygame as py
import random
from enum import Enum


BEAR_ANIMATIONS = [
    EntityAnimationData("bear", "walk", 40, 6, "normal") ,
    EntityAnimationData("bear", "idle", 40, 4, "normal"),
    EntityAnimationData("bear", "death", 40, 6, "normal"),
]

MAGE_ANIMATIONS = [
    EntityAnimationData("mage", "walk", 32, 4, "normal") ,
    EntityAnimationData("mage", "idle", 32, 4, "normal"),
    EntityAnimationData("mage", "death", 32, 6, "normal")
]

OOZE_ANIMATIONS = [
    EntityAnimationData("ooze", "walk", 38, 4, "normal") ,
    EntityAnimationData("ooze", "idle", 38, 4, "normal"),
    EntityAnimationData("ooze", "death", 38, 4, "normal")
]

RED_ANIMATIONS = [
    EntityAnimationData("red", "walk", 32, 6, "normal") ,
    EntityAnimationData("red", "idle", 32, 4, "normal"),
    EntityAnimationData("red", "death", 32, 4, "normal") 
]

TINY_ANIMATIONS = [
    EntityAnimationData("tiny", "walk", 32, 6, "normal") ,
    EntityAnimationData("tiny", "idle", 32, 4, "normal"),
    EntityAnimationData("tiny", "death", 32, 4, "normal") 
]

YELLOW_ANIMATIONS = [
    EntityAnimationData("yellow", "walk", 34, 6, "normal") ,
    EntityAnimationData("yellow", "idle", 34, 4, "normal"),
    EntityAnimationData("yellow", "death", 34, 6, "normal") 
]

ALL_NORMAL_ANIMATIONS = [
    BEAR_ANIMATIONS, MAGE_ANIMATIONS, OOZE_ANIMATIONS, RED_ANIMATIONS, TINY_ANIMATIONS, YELLOW_ANIMATIONS
]

BIG_MUSHROOM_ANIMATIONS = [
    EntityAnimationData("big_mushroom", "walk", 42, 6, "medium") ,
    EntityAnimationData("big_mushroom", "idle", 42, 4, "medium"),
    EntityAnimationData("big_mushroom", "death", 42, 4, "medium")
]

GOBLIN_MAGE_ANIMATIONS = [
    EntityAnimationData("goblin_mage", "walk", 42, 6, "medium") ,
    EntityAnimationData("goblin_mage", "idle", 42, 4, "medium"),
    EntityAnimationData("goblin_mage", "death", 42, 4, "medium")
]

GOBLIN_MELEE_ANIMATIONS = [
    EntityAnimationData("goblin_melee", "walk", 42, 6, "medium") ,
    EntityAnimationData("goblin_melee", "idle", 42, 4, "medium"),
    EntityAnimationData("goblin_melee", "death", 42, 4, "medium")
]

GOBLIN_RANGE_ANIMATIONS = [
    EntityAnimationData("goblin_range", "walk", 42, 6, "medium") ,
    EntityAnimationData("goblin_range", "idle", 42, 4, "medium"),
    EntityAnimationData("goblin_range", "death", 42, 4, "medium")
]

SMALL_MUSHROOM_ANIMATIONS = [
    EntityAnimationData("small_mushroom", "walk", 42, 4, "medium") ,
    EntityAnimationData("small_mushroom", "idle", 42, 4, "medium"),
    EntityAnimationData("small_mushroom", "death", 42, 4, "medium")
]

ALL_MEDIUM_ANIMATIONS = [
    BIG_MUSHROOM_ANIMATIONS, GOBLIN_MAGE_ANIMATIONS, GOBLIN_MELEE_ANIMATIONS, GOBLIN_RANGE_ANIMATIONS, SMALL_MUSHROOM_ANIMATIONS
]

BEHOLDER_ANIMATIONS = [
    EntityAnimationData("beholder", "walk", 42, 4, "hard") ,
    EntityAnimationData("beholder", "idle", 42, 4, "hard"),
    EntityAnimationData("beholder", "death", 42, 4, "hard")
]

DARKGOBLIN_ANIMATIONS = [
    EntityAnimationData("darkgoblin", "walk", 42, 6, "hard") ,
    EntityAnimationData("darkgoblin", "idle", 42, 4, "hard"),
    EntityAnimationData("darkgoblin", "death", 42, 4, "hard")
]

HELLHOUND_ANIMATIONS = [
    EntityAnimationData("hellhound", "walk", 42, 6, "hard") ,
    EntityAnimationData("hellhound", "idle", 42, 4, "hard"),
    EntityAnimationData("hellhound", "death", 42, 6, "hard")
]

HUSKY_ANIMATIONS = [
    EntityAnimationData("husky", "walk", 42, 6, "hard") ,
    EntityAnimationData("husky", "idle", 42, 4, "hard"),
    EntityAnimationData("husky", "death", 42, 4, "hard")
]

SKELETON_ANIMATIONS = [
    EntityAnimationData("skeleton", "walk", 42, 6, "hard") ,
    EntityAnimationData("skeleton", "idle", 42, 4, "hard"),
    EntityAnimationData("skeleton", "death", 42, 4, "hard")
]

ZOMBIE_ANIMATIONS = [
    EntityAnimationData("zombie", "walk", 42, 6, "hard") ,
    EntityAnimationData("zombie", "idle", 42, 4, "hard"),
    EntityAnimationData("zombie", "death", 42, 4, "hard")
]

ALL_HARD_ANIMATIONS = [
    BEHOLDER_ANIMATIONS, DARKGOBLIN_ANIMATIONS, HELLHOUND_ANIMATIONS, HUSKY_ANIMATIONS, SKELETON_ANIMATIONS, ZOMBIE_ANIMATIONS
]

class AllAnimations(Enum):
    NORMAL = ALL_NORMAL_ANIMATIONS
    MEDIUM = ALL_MEDIUM_ANIMATIONS
    HARD = ALL_HARD_ANIMATIONS
    
    
class Difficulty(Enum):
    NORMAL = 5
    MEDIUM = 10
    HARD = 15



class GroundMonstersCreator:
    def __init__(self, count : int) -> None:
        self.count = count
        
        self.word = JsonWordGetter.get()
        self.word_length = len(self.word)
        self.difficulty_monsters = self.set_difficulty_monsters()
        
        
        self.monsters : list[GroundMonster] = []
        
    def set_difficulty_monsters(self) -> list[list[EntityAnimationData]]:
        if self.word_length < Difficulty.MEDIUM.value:
            return AllAnimations.NORMAL.value
        elif self.word_length < Difficulty.HARD.value:
            return AllAnimations.MEDIUM.value
        else:
            return AllAnimations.HARD.value
        
    def add_monsters(self, screen : py.Surface, count : int) -> None:
        for _ in range(count):
            screen_width = screen.get_width()
            monster_type = random.choice(self.difficulty_monsters)
            monster_x = random.randint(0, screen_width - 50)
            
            monster = GroundMonster(monster_x, monster_type)
            
            self.add_new_monster(monster) 
            
    def add_new_monster(self, monster : GroundMonster) -> None:
        self.monsters.append(monster)