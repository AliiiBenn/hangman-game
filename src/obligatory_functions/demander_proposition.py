
"""

4.2.1 


fonction Solitaire

fait par David

"""


def demander_proposition(deja_dit : list[str]) -> str:
    """
    Asks the user for a letter input, validating that the input is a unique, single letter and has not been input before.

    Args:
        deja_dit (list[str]): A list of previously input letters.

    Returns:
        str: A valid, unique letter input by the user.

    """
    deja_dit = [lettre.upper() for lettre in deja_dit]
    
    proposition = input("Entrez une lettre: ").upper()
    
    is_unique_char = len(proposition) == 1
    is_in_deja_dit = proposition in deja_dit
    is_in_ascii = ord(proposition) < 128
    is_letter = proposition >= "A" and proposition <= "Z"
    
    if not is_unique_char or is_in_deja_dit or not is_in_ascii or not is_letter:
        return demander_proposition(deja_dit)
    return proposition   

    

    
    
if __name__ == "__main__":
    
    print(demander_proposition(["a", "b", "c"]))
    