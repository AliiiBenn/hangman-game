
""" 

Doit retourner une liste avec l'ensemble des caracatères majuscules

fonction Solitaire

fait par Lilian

"""


def fabrique_liste_alphabet() -> list[str]:
    """fabrique_liste_alphabet.
        Make a liste with all the letters of the alphabet
    Args:

    Returns:
        list[str]:liste with all the letters of the alphabet 
    """
    ASCII_FOR_A = 65
    ASCII_FOR_Z = 65 + 25
    alphabet : list[str] = []
    current_ascii_code = ASCII_FOR_A
    
    while current_ascii_code <= ASCII_FOR_Z:
        alphabet.append(chr(current_ascii_code))
        current_ascii_code += 1
        
    return alphabet
