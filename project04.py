"""
Author: Kouame Alexandre Paul
Last updated: 09/10/2024 09:30 PM UTC

Program: Word Puzzle Game

Creativity : implemented a select rondom word from the list of string and limitation of the number guesses
"""
import random

print('Welcome to the word guessing game!')
limit_guess = 4
print(f'You have {limit_guess} guesses to use\n')

words = ['mosiah', 'church', "God", "eternal"]

index = random.randint(0, 3)

secret = words[index]

#print(f'Secret {secret}')

hint = ''

#find length of secret
secret_letter_count = len(secret)

#initial hint
for index in range(secret_letter_count):
    hint = hint + "_"

print(f'Your hint is: {hint}')


guess = ''

# while loop to repeat all steps if user did not guesss word
while guess.lower() != secret.lower() and limit_guess >= 1:

    guess = input('What is your guess? ')

    #verify that the length of the guess is the same as the length of the secret word
    if len(guess) == len(secret):

        # Need to convert hint to list. I don't see another simple solution on google
        hint_list = list(hint)

        for secret_index, secret_letter in enumerate(secret):

            for guess_index, guess_letter in enumerate(guess):

                #Check if the letter of secret and guess are same
                if secret_letter.lower() == guess_letter.lower() :

                    #if the letters are same. I check if there are in the same spot
                    if secret_index == guess_index:

                        #if yes, I change letter to uppercase and puts it at the right spot
                        hint_list[guess_index] = guess_letter.upper()

                    else:

                        #if No, I change letter to lowercase in puts it at the right spot of guess string
                        hint_list[guess_index] = guess_letter.lower()

        # I reverse back list to hint string
        #Never set -> hint = ''.join(hint_list) | because it uses as init value for operation
        hint_guess = ''.join(hint_list)
        
        print(f'Your hint is: {hint_guess}')

    else:

        print('Sorry, the guess must have the same number of letters as the secret word.')


    limit_guess = limit_guess - 1

    print(f'it left you {limit_guess} guesses to use')

   

#Game Final Result
if limit_guess <= 1 and guess.lower() != secret.lower(): 

    print('GAME IS OVER. You dont have enough of guesses to continue')

else:
    print('Congratulations! You guessed it!')


