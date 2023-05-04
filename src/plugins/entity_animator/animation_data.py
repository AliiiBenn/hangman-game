from dataclasses import dataclass


@dataclass
class EntityAnimationData:
    monster_name : str
    animation_name : str
    size : int
    images_count : int 
    difficulty : str

    @property
    def image_name(self) -> str:
        return f"{self.monster_name}_{self.animation_name}"