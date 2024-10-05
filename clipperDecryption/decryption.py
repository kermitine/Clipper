import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clipperEncryption.ifArray import *


def clipperDecryption(word, seed):
    seed_index_list = []
    letter_index_list = []
    decrypted_word_list = []
    for char in word:
        letter_index_list.append(character_window_index_str[char])
    print(letter_index_list)
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


print(clipperDecryption('TYQKGSTGAAE', ['21', '07', '20', '14', '03', '04', '11', '17', '18', '25', '08', '13', '01', '15', '02', '16', '24', '26', '12', '05', '19', '23', '06', '09', '10', '22']))