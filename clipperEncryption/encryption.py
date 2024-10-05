from ifArray import *

def clipperEncryption(word, seed):
    seeded_list = []
    encrypted_list = []
    word_list = [char.upper() for char in word]
    for char in word_list:
        window = character_window_index[char]
        seeded_list.append(seed[window])
    for char in seeded_list:
        encrypted_list.append(character_window_inverse_index[char])
    return ''.join(encrypted_list)
print(clipperEncryption('parser', ['21', '07', '20', '14', '03', '04', '11', '17', '18', '25', '08', '13', '01', '15', '02', '16', '24', '26', '12', '05', '19', '23', '06', '09', '10', '22']))