"""
Author: Kouame Alexandre Paul
Last updated: 22/09:24

Program: Converting Fahrenheit to celsus
"""

temp_in_fahrenheit = int(input('What is the temperature in Fahrenheit ? '))
temp_in_celius = (temp_in_fahrenheit - 32) * 5 / 9

print(f"The temperature in Celsius is {temp_in_celius: .1f} degrees.")