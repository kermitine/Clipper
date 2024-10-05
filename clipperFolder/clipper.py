import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clipperDecryption.decryption import *
from clipperEncryption.encryption import *
from seedGeneration.seedGen import *

def sentenceSplitter(sentence):
    split_sentence = sentence.split()
    return split_sentence


print('Clipper V' + version_Decryption + '-' + version_seedGen + '-' + version_Encryption + ' initialized')

seed_word = input('Please enter a seed word. This word will be used to encrypt and decrypt your word.' + '\n')
print('\n' + '\n')

seed = seedGeneration(seed_word)

user_input = input('Enter e for encryption. Enter d for decryption' + '\n')
crypted_list = []
crypted_sentence = ''

if user_input in ['e', 'E']:
    sentence = input('Enter the word you would like to encrypt' + '\n')
    split_sentence = sentenceSplitter(sentence)
    for word in split_sentence:
        crypted_list.append(Encryption(word, seed))
    crypted_sentence = " ".join(crypted_list)
    print(crypted_sentence)

elif user_input in ['d', 'D']:
    sentence = input('Enter the word you would like to decrypt' + '\n')
    split_sentence = sentenceSplitter(sentence)
    for word in split_sentence:
        crypted_list.append(Decryption(word, seed))
    crypted_sentence = " ".join(crypted_list)
    print(crypted_sentence)
