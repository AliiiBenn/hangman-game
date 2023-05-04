from .neural_network import NeuralNetwork 
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from random import randint
import msvcrt as m
from obligatory_functions.initialiser_mot_part_decouv import initialiser_mot_part_decouv
from obligatory_functions.decouvrir_lettre import *
from obligatory_functions.afficher_potence_texte import *
import numpy as np

INPUT_NODES = 26
HIDDEN_NODES = 10
OUTPUT_NODES = 26



def partie_auto_neural():
    word_list = []
    with open("src/neural/word.txt", "r") as f:
        content = f.read()
        word_list = content.split()
    index = randint(0,349)
    mot_myst = word_list[index]
    mot_lettre_cache = initialiser_mot_part_decouv(mot_myst)
    nb_err_max = len(mot_myst)
    nb_err = 0


    # Create the input and output data for training
    X = np.zeros((len(word_list), len(word_list)))
    for i in range(len(word_list)):
        X[i, i] = 1

    # create a neural network and train it
    nn = NeuralNetwork()
    nn.train(X, X, 10000)

    #Play the game
    guesses = []
    play = True
    one_hot_input = X[index].reshape(1, -1)
    predicted_output = nn.predict(one_hot_input)
    predicted_word = word_list[predicted_output]
    
    for letter in predicted_word:
        if not decouvrir_lettre(letter, mot_myst,mot_lettre_cache):
            nb_err += 1
        print(mot_lettre_cache)
        afficher_potence_texte(nb_err,nb_err_max)

        if ''.join(mot_lettre_cache).count('-') == 0:
            break
        if nb_err == nb_err_max:
            break


if __name__ == "__main__":
    partie_auto_neural("thisisatest")
