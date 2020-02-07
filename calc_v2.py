from gematria_dictv2 import *

user_input = input('Give me a word or phrase to get the ordinal gematria in english: ')
word = user_input.lower()

total = 0

for c in word:
	ordinal = ord(c) - 96
	print('{} = {}'.format(c, ordinal))
	total += ordinal

print('Your phrase ordinal gematria sum is: {}'.format(total))
