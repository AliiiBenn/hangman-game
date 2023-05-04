from typing import Optional
import msvcrt as m
from initialiser_mot_part_decouv import *
from decouvrir_lettre import *
from afficher_potence_texte import *


def wait():
    m.getch()

def partie_auto(mot_myst : str, liste_lettres : list[str], affichage : Optional[bool] = True, pause : Optional[bool] = False):

    mot_lettre_cache = initialiser_mot_part_decouv(mot_myst)
    nb_err_max = len(mot_myst)
    nb_err = 0

    for lettre in liste_lettres:
        if affichage == True:
            if pause == True:
                if not decouvrir_lettre(lettre,mot_myst,mot_lettre_cache):
                    nb_err += 1
                print(mot_lettre_cache)
                wait()
                afficher_potence_texte(nb_err,nb_err_max)
            else:
                if not decouvrir_lettre(lettre,mot_myst,mot_lettre_cache):
                    nb_err += 1
                print(mot_lettre_cache)
                afficher_potence_texte(nb_err,nb_err_max)
        else:
                if not decouvrir_lettre(lettre,mot_myst,mot_lettre_cache):
                    nb_err += 1
        if ''.join(mot_lettre_cache).count('-') == 0:
            break
        if nb_err == nb_err_max:
            break


if __name__ == "__main__":
    partie_auto('TEST', ['T','E','S','T'],True,True)
    partie_auto('TEST', ['H','H','H','T'],True,True)
