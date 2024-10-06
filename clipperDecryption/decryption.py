import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vars.ifArray import *
from vars.seedGenVars import *


def Decryption(word, seed, word_count):
    seed_index_list = []
    letter_index_list = []
    decrypted_word_list = []
    
    word = word.upper()
    
     # CLIPPER VARIABLE CIPHERKEY (experimental)

    if word_count != 1:
        if word_count % 2 == 0:
            seed.sort()
        else:
            seed.sort(reverse=True)


    for char in word:
        letter_index_list.append(character_window_index_str[char])
    for letter_index in letter_index_list:
        for seed_index in range(len(seed)):
            print(letter_index, seed[seed_index])
            if letter_index == seed[seed_index]: # if the alphabetical index of the letter matches the seed, take the index of the seed
                seed_index_list.append(seed_index)
                print('match found')
                break
        
    for num in seed_index_list:
        decrypted_word_list.append(character_window_inverse_index_int[num])
    return ''.join(decrypted_word_list)


