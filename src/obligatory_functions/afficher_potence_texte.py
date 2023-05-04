from typing import Final


"""

4.1.4 

Cette fonction doit afficher un texte qui affiche perdu avec un nombre dynamique de !. Elle n'utilise aucune autre fonction du projet

fonction Solitaire

fait par David

"""

def afficher_potence_texte(nb_error : int, nb_error_max : int) -> None:
    """
        Displays a hangman-style text based on the number of errors made.

    Args:
        nb_error (int): The number of errors made.
        nb_error_max (int): The maximum number of errors allowed before losing.

    Returns:
        None

    """
    initial_text = ['-' for _ in range(nb_error_max)] + ['!']
    LOSE_TEXT : Final[str] = "PERDU"
    
    
    for i in range(nb_error):
        if i >= len(LOSE_TEXT):
            initial_text[i] = "!"
        else:
            initial_text[i] = LOSE_TEXT[i]
            
    final_text = "".join(initial_text)
    print(final_text)
    
    
if __name__ == "__main__":
    for i in range(9):
        afficher_potence_texte(i, 8)

    print(list('bonjour'))
