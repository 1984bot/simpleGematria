#ERROR(FIXED) this code only works with 1 word and not multiple. 
# 	      the space between words is counted as a negative number reducing the gematria count making it wrong
#UPDATE, fixed by removing the space between the word

from gematria_dictv2 import *

user_input = input('Give me a word or phrase to get the ordinal gematria in english: ')
word = user_input.lower()
stripped_word = word.replace(" ", "") #replaces all spaces with nothing
total = 0


for c in stripped_word:
    
    ordinal = ord(c) - 96
    print('{} = {}'.format(c, ordinal))
    total += ordinal

print('Your phrase ordinal gematria sum is: {}'.format(total))
