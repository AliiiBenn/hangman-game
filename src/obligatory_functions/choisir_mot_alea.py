import random
from typing import List

def choisir_mot_alea(liste_de_mots: List[str]) -> str:
    index_aleatoire = random.randint(0, len(liste_de_mots) - 1)
    mot_choisi = liste_de_mots[index_aleatoire]
    return mot_choisi
