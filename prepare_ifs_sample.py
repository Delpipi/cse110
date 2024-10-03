"""
Author: Kouame Alexandre Paul
Last updated: 09/29/2024

Program: Great number and Favorite animal
"""
first_nber = int(input("What is the first number? "))
second_nber = int(input("What is the second number? "))

if first_nber > second_nber:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_nber == second_nber:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if first_nber < second_nber:
    print("The second number is greater")
else:
    print("The second number is not greater")

my_animal = "dog"

user_animal = input("\nWhat is your favorite animal? ")
if user_animal.lower() == my_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")