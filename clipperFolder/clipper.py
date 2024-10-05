import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clipperDecryption.decryption import *
from clipperEncryption.encryption import *
from seedGeneration.seedGen import *

print('Clipper V' + version_Decryption + '-' + version_seedGen + '-' + version_Encryption + ' initialized')

seed_word = input('Please enter a seed word. This word will be used to encrypt and decrypt your word.' + '\n')
print('\n' + '\n')

seed = seedGeneration(seed_word)

user_input = input('Enter e for encryption. Enter d for decryption' + '\n')

if user_input in ['e', 'E']:
    word = input('Enter the word you would like to encrypt' + '\n')
    print(Encryption(word, seed))
elif user_input in ['d', 'D']:
    word = input('Enter the word you would like to decrypt' + '\n')
    print(Decryption(word, seed))
