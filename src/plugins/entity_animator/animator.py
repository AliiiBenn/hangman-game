import pygame as py

from .animation_data import EntityAnimationData
from .images_loader import AnimatedEntityImagesLoader
from .errors import InvalidMonsterAnimation


from abc import ABC, abstractmethod


class AnimationStrategy(ABC):
    @abstractmethod
    def play(self, animation_name : str) -> None:
        pass
    
    
class LoopAnimationStrategy(AnimationStrategy):
    def __init__(self, monster_animations_data : list[EntityAnimationData]) -> None:
        self.monster_animations_data = monster_animations_data
        
        self.images_loader = AnimatedEntityImagesLoader(monster_animations_data)
        self.images = self.images_loader.load_images()
        
        self.image = py.Surface([32, 32])
        self.rect = self.image.get_rect()

        self.animation_index = 0
        self.clock = 0
        self.animation_speed = 2

        self.current_animation_name = ""
        
    def play(self, animation_name : str) -> None:
        is_animation_name_valid = animation_name in self.images.keys()
        is_animation_name_different = self.current_animation_name != animation_name
        is_animation_name_empty = self.current_animation_name == ""        
        
        if not is_animation_name_valid:
            monster_name = self.monster_animations_data[0].monster_name
            raise InvalidMonsterAnimation(monster_name, animation_name)
        
        if is_animation_name_different or is_animation_name_empty:
            self.current_animation_name = animation_name
            self.animation_index = 0
        
        self.image = self.images[animation_name][self.animation_index]

        self.image = py.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.image.set_colorkey((0, 0, 0))
        self.clock += self.animation_speed * 8


        if self.clock >= 100:

            self.animation_index += 1

            if self.animation_index >= len(self.images[animation_name]):
                self.animation_index = 0

            self.clock = 0
    
    
class UniqueAnimationStrategy(AnimationStrategy):
    def __init__(self, monster_animations_data : list[EntityAnimationData]) -> None:
        self.monster_animations_data = monster_animations_data
        
        self.images_loader = AnimatedEntityImagesLoader(monster_animations_data)
        self.images = self.images_loader.load_images()
        
        self.image = py.Surface([32, 32])
        self.rect = self.image.get_rect()

        self.animation_index = 0
        self.clock = 0
        self.animation_speed = 2

        self.current_animation_name = ""
    
    def play(self, animation_name : str) -> None:
        is_animation_name_valid = animation_name in self.images.keys()
        
        if self.animation_index >= len(self.images[animation_name]):
            return 
        
        if not is_animation_name_valid:
            monster_name = self.monster_animations_data[0].monster_name
            raise InvalidMonsterAnimation(monster_name, animation_name)
        
        self.image = self.images[animation_name][self.animation_index]

        self.image = py.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.image.set_colorkey((0, 0, 0))
        self.clock += self.animation_speed * 6


        if self.clock >= 100:

            self.animation_index += 1

            self.clock = 0


class AnimatedEntityAnimator:
    def __init__(self, monster_animations_data : list[EntityAnimationData]) -> None:
        self.monster_animations_data = monster_animations_data
        
        self.images_loader = AnimatedEntityImagesLoader(monster_animations_data)
        self.images = self.images_loader.load_images()
        
        self.image = py.Surface([32, 32])
        self.rect = self.image.get_rect()

        self.animation_index = 0
        self.clock = 0
        self.animation_speed = 2

        self.current_animation_name = ""
    
    def change_animation(self, animation_name : str) -> None:
        is_animation_name_valid = animation_name in self.images.keys()
        is_animation_name_different = self.current_animation_name != animation_name
        is_animation_name_empty = self.current_animation_name == ""        
        
        if not is_animation_name_valid:
            monster_name = self.monster_animations_data[0].monster_name
            raise InvalidMonsterAnimation(monster_name, animation_name)
        
        if is_animation_name_different or is_animation_name_empty:
            self.current_animation_name = animation_name
            self.animation_index = 0
        
        self.image = self.images[animation_name][self.animation_index]

        self.image = py.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.image.set_colorkey((0, 0, 0))
        self.clock += self.animation_speed * 8


        if self.clock >= 100:

            self.animation_index += 1

            if self.animation_index >= len(self.images[animation_name]):
                self.animation_index = 0

            self.clock = 0
            
            
    def play_unique_animation(self, animation_name : str) -> None:
        is_animation_name_valid = animation_name in self.images.keys()
        
        if self.animation_index >= len(self.images[animation_name]):
            return 
        
        if not is_animation_name_valid:
            monster_name = self.monster_animations_data[0].monster_name
            raise InvalidMonsterAnimation(monster_name, animation_name)
        
        self.image = self.images[animation_name][self.animation_index]

        self.image = py.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.image.set_colorkey((0, 0, 0))
        self.clock += self.animation_speed * 6


        if self.clock >= 100:

            self.animation_index += 1

            self.clock = 0
            
            