from seedGeneration.seedGenVars import *


def seedGeneration(seed_word):
    seed = []
    num_dict = 1
    seed_word_list = [x.upper() for x in seed_word] # splits seed_word into uppercase list

    for char in seed_word_list: # uses seed_generation__index dict to convert letter to number
        seed.append(seed_generation_index[char])

    if len(seed) < 26:
        for x in range(26 - len(seed)): # add numbers until len = 26

            if seed_generation_number_index[num_dict] in seed: # if dict number is already in seed, move on
                num_dict += 1
                pass

            seed.append(seed_generation_number_index[num_dict]) 
            num_dict += 1
            
    return seed


print(seedGeneration('Radioimmunoelectrophoresis'))
