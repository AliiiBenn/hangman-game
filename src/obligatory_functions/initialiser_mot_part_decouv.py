from typing import Optional

"""

4.1.3

Il faut créer une fonction qui retourne une liste contenant la première et la dernière lettre d'un mot mystère avec toutes les 
autres lettres cachées par un caractère

fonction Solitaire

fait par 


"""


def initialiser_mot_part_decouv(mot_myst : str, car_subst : Optional[str] = "-") -> list[str]:
    """initialiser_mot_part_decouv.
        Renvoie le mot à deviner avec toutes les lettres cacher sauf la premiere et derniere
    Args:
        mot_myst (str): le mot à deviner
        car_subst (Optional[str]):caractere qui remplace les lettres, sauf la derniere et la premiere, du mot a deviner 

    Returns:
        list[str]:liste des lettres du mot a deviner avec toutes les lettres remplacer par car_subst sauf la premier et derniere
    """
    splitAndSubstList = []
    for index, element in enumerate(mot_myst):
        if index == 0 or index == len(mot_myst) - 1:
            splitAndSubstList.append(element)
        else:
            splitAndSubstList.append(car_subst) #type: ignore


    return splitAndSubstList


if __name__ == "__main__":
    mot = "BONJOUR"
    print(initialiser_mot_part_decouv(mot))
