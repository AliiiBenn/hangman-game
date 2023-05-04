from typing import Optional

from obligatory_functions.importer_mots import importer_mots
from obligatory_functions.choisir_mot_alea import choisir_mot_alea
from obligatory_functions.partie_humain import partie_humain

def partie_humain_alea(nom_fichier : str, nb_error_max : int, car_subst : Optional[str] = "-") -> bool:
    mots = importer_mots(nom_fichier)
    mot_a_decouv = choisir_mot_alea(mots)

    return partie_humain(mot_a_decouv, nb_error_max, car_subst)


if __name__ == "__main__":
    p = partie_humain_alea("mots2.txt", 8)
    if p:
        print("gagné")
    else:
        print("perdu")
