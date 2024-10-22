"""
Author: Kouame Alexandre Paul
Last updated: 15/10/2024 09:40 PM UTC

Program: Practice using lists and list indexes.
"""

items = []
item = ''

print('\nPlease enter the items of the shopping list (type: quit to finish): ')
while item != 'quit':
    if item != '':
        items.append(item)
    item = input('Item: ')

print('\nThe shopping list is:')
for element in items:
    print(element)

print('\nThe shopping list with indexes is:')
for i in range(len(items)):
    print(f'{i}. {items[i]}')

print()
index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')

for i in range(len(items)):
    if i == index:
        items[i] = new_item

print('\nThe shopping list with indexes is:')
for i in range(len(items)):
    print(f'{i}. {items[i]}')

