import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clipperDecryption.decryption import *
from clipperEncryption.encryption import *
from seedGeneration.seedGen import *
from vars.globalVars import *
from vars.ascii import *

ascii_run()

print('Clipper V' + version_Clipper + '-' + version_Decryption + '-' + version_seedGen + '-' + version_Encryption + ' initialized' + '\n')


def sentenceSplitter(sentence):
    split_sentence = sentence.split()
    return split_sentence

def mainClipper():
    word_count = 0

    seed_word = input('Please enter a seed word/phrase. This string will be used to encrypt and decrypt your phrase.' + '\n')
    print('\n')

    seed = seedGeneration(seed_word)

    user_input = input('Enter e for encryption. Enter d for decryption:' + '\n')
    print('\n' + '\n')
    crypted_list = []
    crypted_sentence = ''

    if user_input in ['e', 'E']:
        sentence = input('Enter the word you would like to encrypt:' + '\n')
        print('\n' + '\n')
        split_sentence = sentenceSplitter(sentence)
        for word in split_sentence:
            word_count += 1
            crypted_list.append(Encryption(word, seed, word_count))
        crypted_sentence = " ".join(crypted_list)
        print('Encrypted Result:' + '\n')
        print(crypted_sentence)

    elif user_input in ['d', 'D']:
        sentence = input('Enter the word you would like to decrypt:' + '\n')
        print('\n' + '\n')
        split_sentence = sentenceSplitter(sentence)
        for word in split_sentence:
            word_count += 1
            crypted_list.append(Decryption(word, seed, word_count))
        crypted_sentence = " ".join(crypted_list)
        print('\n')
        print('Decrypted Result:' + '\n')
        print(crypted_sentence)
    else:
        print('Input not recognized. Assuming encryption.')
        sentence = input('Enter the word you would like to encrypt:' + '\n')
        print('\n' + '\n')
        split_sentence = sentenceSplitter(sentence)
        for word in split_sentence:
            word_count += 1
            crypted_list.append(Encryption(word, seed, word_count))
        crypted_sentence = " ".join(crypted_list)
        print('Encrypted Result:' + '\n')
        print(crypted_sentence)

while True:
    mainClipper()
    print('\n' + '\n')
    user_code = input('Enter t to translate another sentence. Enter anything else to exit' + '\n')
    print('\n' + '\n')
    if user_code in ['t', 'T']:
        pass
    else:
        break