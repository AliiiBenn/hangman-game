
"""
4.1.1 

On doit créer une fonction qui va chercher tous les mots dans un fichier .txt et qui retourne une liste de ces mots.
Elle utilise aucune autre fonction du projet. 

fonction Solitaire 

fait par David

"""

def importer_mots(nom_fichier : str) -> list[str]: 
    """
    Imports a list of words from a given file.

    Args:
        nom_fichier (str): The name of the file to import the words from.

    Returns:
        list[str]: A list of words imported from the file.

    """
    with open(nom_fichier, "r") as fichier:
        liste_mots = fichier.readlines()
        
    mots : list[str] = []
    
    for mot in liste_mots:
        if not len(mot) < 3:
            mots.append(mot.strip().upper())
    
    return mots





if __name__ == "__main__":
    print(importer_mots("texts\\test.txt"))