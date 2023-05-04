from typing import Optional
from .initialiser_mot_part_decouv import *
from .decouvrir_lettre import *
from .afficher_potence_texte import *
from .dico_frequence import *
from .fabrique_liste_freq import fabrique_liste_freq
from random import randint



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

    return nb_err
def call_partie_auto(mot_myst : str, affichage : Optional[bool] = True, pause: Optional[bool] = False):
    random_num = randint(0,2)

    print(random_num)
    if random_num == 0:
        dico = dico_frequence("./src/obligatory_functions/mots2.txt")
        treshold = 5
        list = []
        for key, value in dico.items():
            if value >= treshold:
                list.append(key)
        partie_auto(mot_myst, list, affichage, pause)

    if random_num == 1:
        list = fabrique_liste_freq("./src/obligatory_functions/mots2.txt")
        partie_auto(mot_myst, list, affichage, pause)
    else:
        alphabet = []

        for i in range(ord('a'), ord('z') + 1):
            alphabet.append(chr(i))

        partie_auto(mot_myst, alphabet, affichage, pause)




if __name__ == "__main__":
    call_partie_auto('OUI',True,True)
    call_partie_auto('OUI',True,True)

