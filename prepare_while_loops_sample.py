"""
Author: Kouame Alexandre Paul
Last updated: 06/10/2024 08:41 UTC

Program: while loops sample
"""
#ask the user for a positive number (>= 0).
number = int(input('Please type a positive number: '))

while number < 0:
    print('Sorry, that is a negative number. Please try again')
    number = int(input('Please type a positive number: '))

print(f'The numer is: {number}')

#asking parent for a piece of candy
answer = ""

while answer.lower() != 'yes':
    answer = input('May I have a piece of candy? ')

print('Thank you')