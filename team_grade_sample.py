"""
Author: Kouame Alexandre Paul
Last update: 09/29/2024 20:49

Program: Letter grade
"""

grade = int(input('What is your grade percentage (%)? '))

sign = ''
letter = "F"

#compute last digit of grade
last_digit = grade % 10
#print(f'LAST DIGIT: {last_digit}')

#Find grade
if grade >= 90 :
    letter = "A"
elif grade >= 80 and grade < 90 :
    letter = "B"
elif grade >= 70 and grade < 80 :
    letter = "C"
elif grade >= 60 and grade < 70 :
    letter = "D"
else:
    letter = "F"

#Find grade sign
if last_digit >= 7 :
    sign = '+'
else:
    if last_digit < 3 :
        sign = '-'
    else:
        sign = ''

print()
print(f'Your grade is : {letter}{sign}({grade}%)')

print()

if grade >= 70 :
    print('Your can passed the class')
else:
    print('Sorry, you can not passe the class')