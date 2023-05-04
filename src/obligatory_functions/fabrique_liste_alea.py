
""" 

Fait par Lilian


"""
import random


def fabrique_list_alea() -> list[str]:
    """fabrique_list_alea.
        Make a list with all the letters of the alphabet and shuffle it 
    Args:

    Returns:
        list[str]:all letters of the alphabet in a random order
    """
    alphabet = fabrique_list_alea()
    random.shuffle(alphabet)

    return alphabet
