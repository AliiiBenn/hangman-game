
from importer_mots import importer_mots


def dico_frequence(nom_fichier : str) -> dict[str, int]:
    """dico_frequence.
        Creer un dictionnaire avec la frequence d'apparition de chaque lettres
    Args:
        nom_fichier (str):input file 

    Returns:
        dict[str, int]:dictionnaire contenant la frequence de chaque lettres
    """
    # import zords from file (use importer_mots function)
    words = importer_mots(nom_fichier)

    #we converted the list of strings into a single strings
    # it cost O(n) but with the whole algorithm
    # will cost O(2n) instead of O(n^2)
    string_converted_words = ''.join(words)

    frequence_dict : dict[str, int] = {}

    for letter in string_converted_words:
        if letter in frequence_dict:
            frequence_dict[letter] += 1
        else:
            frequence_dict[letter] = 1

    return frequence_dict

