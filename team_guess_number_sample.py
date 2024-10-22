"""
Author: Kouame Alexandre Paul
Last updated: 09/10/2024 08:49 PM UTC

Program: Guess My Number Game
"""
import random

#Requirement 1: ask user maggic number
# maggic = int(input('What is the maggic number? '))
# guess = int(input('What is your guess? '))

# if guess < maggic:
#     print('Higher')
# elif guess > maggic:
#     print('Lower')
# else:
#     print('You guessed it !')

#print()

#Requirement 2: ask user maggic number
# answer = 'yes'

# while answer.lower() == 'yes':

#     track = 4
#     maggic = int(input('What is the maggic number? '))
#     guess = int(input('What is your guess? '))

#     while guess != maggic and track > 0:
#         if guess < maggic:
#             print('Higher')
#         if guess > maggic:
#             print('Lower')
#         track = track - 1
#         print(f'you have {track} try again')
#         guess = int(input('What is your guess? '))

#     #when user guessed the number. it means that the track not equal null
#     if track == 0:
#         print('Guess number not found. GAME IS OVER')
#     else:
#         print('You guessed it !')

#     answer = input('Do you want to play again? ')

#Requirement 3: use random number from 1 to 10 as maggic number
answer = 'yes'

while answer.lower() == 'yes':

    track = 4
    maggic = random.randint(1, 10)
    guess = int(input('\nWhat is your guess? '))

    while guess != maggic and track > 0:
        
        if guess < maggic:
            print('Higher')
        if guess > maggic:
            print('Lower')

        track = track - 1
        print(f'you have {track} try again')
        
        guess = int(input('\nWhat is your guess? '))

    #when user guessed the number. it means that the track not equal null
    if track == 0:
        print('Guess number not found. GAME IS OVER')
    else:
        print('You guessed it !')

    answer = input('\nDo you want to play again (yes/no)? ')

print('Thanks for playing our guess game. see you soon')