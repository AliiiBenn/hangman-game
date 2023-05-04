import pygame  
from pygame import mixer, font
from game import Game



def main() -> None:
    pygame.init()
    mixer.init()
    font.init()
    game = Game(1000, 600)
    game.load_extentions()
    game.run()


if __name__ == "__main__":
    main()
