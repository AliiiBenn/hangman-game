import pygame, time
from pygame import mixer, font
from game import Game
from pypattyrn.creational.factory import Factory
from enum import Enum, auto
from abc import ABC, abstractstaticmethod


class GameTypeStrategy(ABC):
    @abstractstaticmethod
    def play() -> None:
        pass

class GraphicGameStrategy(GameTypeStrategy):
    @staticmethod
    def play() -> None:
        pygame.init()
        mixer.init()
        font.init()
        game = Game(1000, 600)
        game.load_extentions()
        game.run()  

class GameType(Enum):
    HUMAN = auto()
    HUMAN_RANDOM = auto()
    AUTO = auto()
    GRAPHIC = auto()
    NEURAL = auto()


class IncorrectGameType(Exception):
    def __init__(self, game_type : GameType) -> None:
        """Exception raised when the game mode is incorrect"""
        super().__init__(f"The game type {game_type} is incorrect.", game_type)



class GameModeFactory(Factory):
    @staticmethod
    def create(game_mode_type : GameType) -> GameTypeStrategy:
        if game_mode_type == GameType.GRAPHIC:
            return GraphicGameStrategy()
        else:
            raise IncorrectGameType(game_mode_type)


class GameMenuModel:
    def ask_for_game_type(self, choice_types : dict[int, GameType]) -> GameType:        
        choice = None
        
        while choice is None:
            try:
                current_choice = int(input("Veuillez choisir votre mode de jeu : "))
                choice = choice_types[current_choice]
            except KeyError:
                choice = None

        return choice


    def run_game_based_on_choice(self, choice : GameType) -> None:
        game_mode = GameModeFactory.create(choice)

        return game_mode.play()


class GameMenuView:
    def render_menu_message(self) -> None:
        print("----- Mode de Jeu -----\n")
        print("1- Partie humain")
        print("2- Partie aléatoire")
        print("3- Partie auto")
        print("4- Partie Graphique")
        print("5- Partie auto neural network")
        print("\n----------------------")

    def render_choice_message(self, choice : GameType) -> None:
        if choice == GameType.HUMAN:
            print("Vous avez choisi la partie Humain, vous allez donc jouer dans le terminal.")
        elif choice == GameType.HUMAN_RANDOM:
            print("Vous avez choici la partie Random, Vous allez jouer dans le terminal avec un mot aléatoire.")
        elif choice == GameType.AUTO:
            print("Vous avez choisi la partie auto, la machine va donc jouer à votre place.")
        elif choice == GameType.GRAPHIC:
            print("Vous avez choisi la partie graphique, vous allez donc jouer sur une interface graphique.")
        elif choice == GameType.NEURAL:
            print("Vous avez choisi la partie auto par AI neural network, la machine va donc jouer à votre place.")
        else:
            raise IncorrectGameType(choice)


class GameMenuController:
    def __init__(self, model : GameMenuModel, view : GameMenuView) -> None:
        self.model = model 
        self.view = view 


    def start(self) -> None:
        self.view.render_menu_message()


        choice_types : dict[int, GameType] = {
            1 : GameType.HUMAN,
            2 : GameType.HUMAN_RANDOM,
            3 : GameType.AUTO,
            4 : GameType.GRAPHIC,
            5 : GameType.NEURAL
        }

        choice = self.model.ask_for_game_type(choice_types)
        self.view.render_choice_message(choice)

        time.sleep(2) # Fake game load because why not
        self.model.run_game_based_on_choice(choice)




if __name__ == "__main__":
    game_menu = GameMenuController(GameMenuModel(), GameMenuView())

    game_menu.start()
