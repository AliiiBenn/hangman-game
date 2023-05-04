from .dico_frequence import *
from .lettre_la_plus_frequente import *


""" 

fait par Lilian

"""

def fabrique_liste_freq(nom_fichier):
    """fabrique_liste_freq.
        Fabrique une liste de la lettre la plus frequente a la moin frequente

    Args:
        nom_fichier: fichier contenant les mots 
            """
    dico = dico_frequence(nom_fichier)
    liste = []
    while dico:
      letter = lettre_la_plus_frequente(dico)
      liste.append(letter)
      del dico[letter]
    return liste
