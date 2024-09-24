"""
Author: Kouame Alexandre Paul
Last update: 18/09/2024 9:35 PM UTC

Program: Clever Stories
"""

print('Please enter the following:')
print()

adjective = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')

#add custom variable to get user favorite pet and article to be a or an
pet = input('pet: ')
article = 'a'

#Check if the first letter of pet is vowel. if yes put 'an' before else 'a'
if pet[0] in ['a','e','i','o','u']:
    article = 'an'


output1 = f"""The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously, 
that caused it to stop, but not before it tried to {verb3}
right in front of my family."""

#Creativity
output2 = f"""The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation.title()}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously, thanks to {article} {pet}
that caused it to stop, but not before it tried to {verb3}
right in front of my family."""

print()
print('Your story is: ')
print()
print(output1)

print()
print(output2)