import pygame as py

from .animation_data import EntityAnimationData
from .image_cutter import AnimatedEntityImageCutter


class AnimatedEntityImagesLoader:
    def __init__(self, monster_animations_data : list[EntityAnimationData]) -> None:
        self.monster_animations_data = monster_animations_data
    
    def load_images(self) -> dict[str, list[py.surface.Surface]]:
        images_dict : dict[str, list[py.surface.Surface]] = {}

        for animation_data in self.monster_animations_data:
            images_dict[animation_data.animation_name] = AnimatedEntityImageCutter.get_images(animation_data)

        return images_dict