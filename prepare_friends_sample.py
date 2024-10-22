"""
Author: Kouame Alexandre Paul
Last updated: 15/10/2024 09:20 PM

Program: List of friend name
"""
friends = []
name = ''

while name != 'end':
    if name != '':
        friends.append(name)
    name = input('Type the name of a friend: ')

print('\nYour friends are: ')
for friend in friends:
    print(friend)

