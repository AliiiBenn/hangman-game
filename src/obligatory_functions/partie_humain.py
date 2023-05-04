from typing import Optional

from decouvrir_lettre import decouvrir_lettre
from initialiser_mot_part_decouv import initialiser_mot_part_decouv
from afficher_potence_texte import afficher_potence_texte
from demander_proposition import demander_proposition


""" 

Fait par David

"""

def partie_humain(mot_myst : str, nb_error_max : int, car_subst : Optional[str] = "-") -> bool:
    gagne = False
    perdu = False
    nb_error = 0
    deja_dit : list[str] = []
    mot_a_decouv = initialiser_mot_part_decouv(mot_myst, car_subst)
    while not gagne and not perdu:
        print(mot_a_decouv)
        if len(deja_dit) >= 1:
            print(deja_dit)

        proposition = demander_proposition(deja_dit)

        dans_mot = decouvrir_lettre(proposition, mot_myst, mot_a_decouv)
        if not dans_mot:
            nb_error += 1
            if nb_error >= nb_error_max:
                perdu = True
            else:
                afficher_potence_texte(nb_error, nb_error_max)
            

        if ''.join(mot_a_decouv).count(car_subst) == 0:
            gagne = True 

    return gagne



if __name__ == "__main__":
    p = partie_humain("BONJOUR", 8)
    if p:
        print("Gagné")
    else:
        print("Perdu")