"""

4.2.2 

fonction Solitaire

fait par Lilian

"""


def decouvrir_lettre(lettre: str, mot_myst: str, lmot_decouv: list[str]) -> bool:
    """decouvrir_lettre.
        Prend une lettre et regarde si elle est présente dans un mot et ajoute cette lettre a chaque emplacement dans la liste du mot partiellement découvert.

    Args:
        lettre (str): lettre proposée par le joueur
        mot_myst (str): mot a deviner
        lmot_decouv (list[str]): mot partiellement découvert

    Returns:
        bool:Si oui ou non la lettre est dans le mot_myst
    """
    lettre = lettre.upper()
    mot_myst = mot_myst.upper()
    isInMot = False
    for i in range(1, len(mot_myst) - 1):     
        if mot_myst[i] == lettre:
            lmot_decouv[i] = lettre
            isInMot = True
    return isInMot

if __name__ == "__main__":
    liste = ["B", "-", "-", "-", "-", "-", "R"]
    print(decouvrir_lettre("O", "BONJOUR", liste))
    print(liste)
    print(decouvrir_lettre("R", "bonjour", liste))
    print(liste)
