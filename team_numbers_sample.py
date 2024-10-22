"""
Author: Kouame Alexandre Paul
Last updated: 16/10/2024 11:53 PM UTC

Program: Sum of list of number
"""
numbers = []

#Get list of numbers
num = -1
print('Enter a list of numbers, type 0 when finished.')
while num != 0:
    num = int(input('Enter number: '))
    if num != 0 :
        numbers.append(num)
   

#Find sum of numbers
sum = 0
for nber1 in numbers:
    sum = sum + nber1
print(f'The sum is : {sum}')

#Compute average of the numbers
avg = sum / len(numbers)
print(f'The average is : {avg}')

#Find the largest number
largest_number = -1
for nber2 in numbers:
    if nber2 > largest_number:
        largest_number = nber2

print(f'The largest number is: {largest_number}')

#init variable to store smallest positive number
smallest_positive = 9999999999
for nber3 in numbers:
    if nber3 > 0 and nber3 < smallest_positive:
        smallest_positive = nber3

print(f'The smallest positive number is: {smallest_positive}')

#Sort the numbers in the list
sort_list = sorted(numbers)
print('The sorted list is: ')
for nber4 in sort_list:
    print(nber4)