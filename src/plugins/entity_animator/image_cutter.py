import pygame as py

from .animation_data import EntityAnimationData
from .image_surface_creator import AnimatedEntityImageSurfaceCreator

class AnimatedEntityImageCutter:
    @staticmethod
    def get_images(animation_data : EntityAnimationData) -> list[py.surface.Surface]:
        images : list[py.surface.Surface] = []

        for i in range(animation_data.images_count):
            x = i * animation_data.size
            image = AnimatedEntityImageSurfaceCreator.get_image(x, animation_data.size, animation_data.image_name, animation_data.difficulty)
            images.append(image)

        return images