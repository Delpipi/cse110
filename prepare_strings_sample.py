"""
Author: Kouame Alexandre Paul
Last updated: 09/10/2024 08:21 PM

Program: Find favorite letter
"""
word = "Good morning Alexander"
favorite_letter = "m"

#print letter "m" in Capital. others to lowercase
for letter in word:
    if favorite_letter == letter:
        print(favorite_letter.upper())
    else:
        print(letter.lower())

favorite_letter = input('\nwhat is your favorite letter? ')

#print favorite letter in Capital. others to lowercase
for letter in word:
    if favorite_letter.lower() == letter.lower():
        print(favorite_letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

#Hide favorite letter with underscore. others to lowercase
for letter in word:
    if favorite_letter.lower() == letter:
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()