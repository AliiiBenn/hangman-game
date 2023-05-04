import pygame as py
import random


from plugins.entity_animator.animation_data import EntityAnimationData
from plugins.entity_animator.animator import AnimatedEntityAnimator


from plugins.monsters.monsters_directions import Direction
from plugins.monsters.direction_timer import DirectionTimer
    


class GroundMonster(AnimatedEntityAnimator):
    def __init__(self, x : int, animation_data : list[EntityAnimationData]) -> None:
        super().__init__(animation_data)
        self.x = x

        self.direction = random.choice(list(Direction))
        
        self.dead = False
        
        self.repeat_move = random.randint(1000, 3000)
        self.timer = DirectionTimer(self.repeat_move)

    
    def update(self, screen : py.Surface) -> None:
        if self.timer.check() and not self.dead:
            self.direction = random.choice(list(Direction))
        
        self.draw(screen)
        if not self.dead:
            self.move(1)
        else:
            self.play_unique_animation("death")
        
    def draw(self, screen : py.Surface) -> None:
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = screen.get_height() - 128 - self.image.get_height()
        
        screen.blit(py.transform.flip(self.image, self.direction == Direction.RIGHT, False), self.rect)
        
        
    def move(self, moving_speed : int) -> None:         
        if self.direction == Direction.RIGHT or self.direction == Direction.LEFT:
            self.x += moving_speed * self.direction.value 
            self.change_animation("walk")
           
        elif self.direction == Direction.NONE:
            self.change_animation("idle")
            
            

            
            


        
            
            

            
            

        
            

            
