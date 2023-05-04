import pygame as py 

from plugins.word.word_displayer import WordDisplayer

from game import factory

class Flush:

    def __init__(self, x : int, y : int )->None:
        self.word = ""
        self.displayer = WordDisplayer(self.word, x, y)

    def update(self, screen : py.Surface) -> None:
        self.displayer.draw(screen)


def register():
    return factory.register("Flush", Flush)
