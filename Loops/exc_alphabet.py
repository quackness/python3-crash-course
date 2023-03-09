# for index,letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
#   print(letter + " is the " + str(index + 1) + "th letter of the alphabet")

  # to be continued 


#2
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lphbt = alphabet #vowels taken out
vowels = 'aeiou'

for vowel in vowels:
    lphbt = lphbt.replace(vowel, '')

print(lphbt)

favoriteAlphabet = alphabet
favoriteLetters = 'gsbrox'

for letter in favoriteLetters:
  favoriteAlphabet = favoriteAlphabet.replace(letter, letter.upper())
print(favoriteAlphabet)
