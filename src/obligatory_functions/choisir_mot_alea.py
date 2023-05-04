"""

4.1.2

On doit créer une fonction qui choisi un mot parmis une liste de mot de façon aléatoire, elle n'utilise aucune autre fonction du projet

fonction Solitaire

fait par Lilian

"""

import random


def choisir_mot_alea(liste_mots: list[str]) -> str:
    """choisir_mot_alea.
        Choisis un mot au hasard dans une liste
    Args:
        liste_mots (list[str]): liste de mots possible dans le jeu 

    Returns:
        str:Mot choisis au hasard dans la liste
    """
    randomNumber = random.randint(0, len(liste_mots) - 1)



    return liste_mots[randomNumber]
