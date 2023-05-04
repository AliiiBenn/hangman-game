
""" 

Fait par Lilian


"""
import random

from .fabrique_liste_alphabet import fabrique_liste_alphabet


def fabrique_liste_alea() -> list[str]:
    """fabrique_list_alea.
        Make a list with all the letters of the alphabet and shuffle it 
    Args:

    Returns:
        list[str]:all letters of the alphabet in a random order
    """
    alphabet = fabrique_liste_alphabet()
    random.shuffle(alphabet)

    return alphabet
