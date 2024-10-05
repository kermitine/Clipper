
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vars.ifArray import *
from vars.seedGenVars import *

def Encryption(word, seed):
    seeded_list = []
    encrypted_list = []
    word_list = [char.upper() for char in word] # converts word_list to uppercase
    for char in word_list:
        window = character_window_index[char] # converts each 'letter' to its alphabetical index (A = 1, B = 2, etc)
        seeded_list.append(seed[window]) 
    for char in seeded_list:
        encrypted_list.append(character_window_inverse_index[char]) # converts the 1-26 seed back into a letter
    return ''.join(encrypted_list)
