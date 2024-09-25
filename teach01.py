"""
Author : Kouame Alexandre Paul
Last update : 18/09/2024

Program: ID badge Generator
"""
print('Please enter the following information:')
print()
first_name = input('First name: ')

last_name = input('Last name: ')

email = input('Email address: ')

phone_number = input('Phone number: ')

job_title = input('Job title: ')

id_number = input('ID Number: ')

#stretch challenge
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')

month_name = input('Month name: ')
training = input('Completed additional training (yes/no): ')

print()
#Display Information without formatting
print('Your information are:')
print(last_name)
print(first_name)
print(email)
print(phone_number)
print(job_title)
print(id_number)

#Stretch Challenge
print()
print(hair_color)
print(eye_color)
print(month_name)
print(training)

print()
#Display Information with formatting
print('The ID card is:')
print('-'*30)
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(job_title.title())
print(f'ID: {id_number} \n')
print(email.lower())
print(phone_number)
print()
#(:<10) left align  hair_color and month_name in space of 10 characters
print(f'Hair: {hair_color.title():<10} Eyes: {eye_color.title()}')
print(f'Month: {month_name.title():<10} Training: {training.title()}')
print('-'*30)