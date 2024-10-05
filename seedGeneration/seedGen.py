import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vars.ifArray import *
from vars.seedGenVars import *


def seedGeneration(seed_word):
    seed = []
    num_dict = 1
    pop_list = []

    print('Starting seed generation...')

    seed_word_list = [x.upper() for x in seed_word] # splits seed_word into uppercase list
    for x in range(len(seed_word_list)):
        if seed_word_list[x] in special_characters_list or seed_word_list[x] == ' ':
            pop_list.append(x)

    
    pop_list.sort(reverse=True)

    for x in pop_list:
        seed_word_list.pop(x)


    if len(seed_word_list) > 26:
        print('Word sliced')
        seed_word_list = seed_word_list[:26]


    seed_word_list = list(dict.fromkeys(seed_word_list))  # removes duplicate letters (no idea how this works but it does)

    print('Purging duplicates')

    for char in seed_word_list: # uses seed_generation__index dict to convert letter to number
        seed.append(seed_generation_index[char])

    print('Converting text to numerics')


    if len(seed) < 26: # if seed is not long enough
        while len(seed) < 26:
            if num_dict > 26:
                num_dict = 1
            if seed_generation_number_index[num_dict] not in seed:
                seed.append(seed_generation_number_index[num_dict])
                num_dict += 1
                pass
            num_dict += 1

    print('Finalizing' + '\n')

    print('Generated seed:')
    print(''.join(seed) + '\n')
    return seed
