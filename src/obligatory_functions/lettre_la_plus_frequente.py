

def lettre_la_plus_frequente(dico : dict[str, int]) -> str:
    most_frequent_letter = ""
    maximum_occurence = 0
    
    for letter, occurence in dico.items():
        if occurence > maximum_occurence:
            maximum_occurence = occurence
            most_frequent_letter = letter
            
    return most_frequent_letter

