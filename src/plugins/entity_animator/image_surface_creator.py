import pygame as py


def load_monster(difficulty : str, image_name : str) -> py.surface.Surface:
    """Load the monster image"""
    return py.image.load(f"assets/monsters/{difficulty}_monsters/{image_name}.png")

def create_image(size : list[int], sprite_sheet : py.surface.Surface, x : int, y : int) -> py.surface.Surface:
    image = py.Surface(size)
    image.blit(sprite_sheet, (0, 0), (x, y, size[0], size[1]))
    
    return image


class AnimatedEntityImageSurfaceCreator:
    @staticmethod
    def get_image(x : int, size : int, image_name : str, difficulty : str) -> py.surface.Surface:
        sprite_sheet = load_monster(difficulty, image_name)
        
        return create_image([size, size], sprite_sheet, x, 0)
