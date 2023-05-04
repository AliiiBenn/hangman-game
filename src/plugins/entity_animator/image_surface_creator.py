import pygame as py


class AnimatedEntityImageSurfaceCreator:
    @staticmethod
    def get_image(x : int, size : int, image_name : str, difficulty : str) -> py.Surface:
        sprite_sheet = py.image.load(f"assets\\monsters\\{difficulty}_monsters\\{image_name}.png")
        image = py.Surface([size, size])
        image.blit(sprite_sheet, (0, 0), (x, 0, size, size))

        return image