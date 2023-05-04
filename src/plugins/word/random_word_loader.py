import random
import os


def importer_mots(nom_fichier : str) -> list[str]:
    
    with open(nom_fichier, "r") as file:
        words = file.readlines()

    new_words : list[str] = []

    for word in words:
        if len(word) >= 3:
            new_words.append(word.strip().lower())

    return new_words

def choisir_mot_alea(liste_mots: list[str]) -> str:
    """choisir_mot_alea.
        Choisis un mot au hasard dans une liste
    Args:
        liste_mots (list[str]): liste de mots possible dans le jeu 

    Returns:
        str:Mot choisis au hasard dans la liste
    """
    random_number = random.randint(0, len(liste_mots) - 1)

    return liste_mots[random_number]
    
def load_random_word(file_name : str) -> str:
    """Load the word file and pick a random word

    Args:
        file_name (str): The name of the file to load

    Returns:
        str: The random word
    """
    words = importer_mots(file_name)

    RANDOM_WORD = choisir_mot_alea(words)

    return RANDOM_WORD

