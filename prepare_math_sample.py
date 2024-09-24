"""
 Author: Kouame Alexandre Paul
 Last updated: 22/09/2024

 Program: compute numeric variable
"""

age = int(input('How old are you ? '))
next_age = age + 1
print('On your next birthday, you will be ' + str(next_age))
print()
egg_cartons = int(input('How many egg cartons do you have ? '))
eggs = egg_cartons * 12
print('You have ' + str(eggs))
print()
cookies = int(input('How many cookies do you have ? '))
people = int(input('How many people are there ? '))
cookies_per_person = cookies / people
print(f'Each person may have {cookies_per_person} cookies')