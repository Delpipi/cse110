"""
  Author: Kouame Alexandre Paul
  Last updated: 09/22/2024 8:07 PM UTC

  Program: Compute area of Square, Rectangle and Circle

  For the stretch challenges part.We will import "math" library and will use
  its build-in value "math.pi"
"""
#Area of square
side = float(input('What is the length of a side of the square? '))
area_of_square = side ** 2
print(f"The area of the square is : {area_of_square}")

#Area of a rectangle
length = float(input('What is the length of rectangle? '))
width = float(input('What is the width of the rectangle? '))
area_of_rectangle = length * width
print(f"The area of the rectangle is : {area_of_rectangle}")

#Area of a circle
radius = float(input('What is the radius of the circle? '))
area_of_circle = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area_of_circle}")

print()
# Stretch 1: Using the math library
import math
radius = float(input('What is the radius of the circle? '))
area_of_circle = math.pi * (radius ** 2)
print(f"The area of the circle is: {area_of_circle}")

#Stretch 2: Many areas from one value
value = float(input('Give the length value: '))

area_square = value ** 2 
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
voume_sphere = (4/3) * math.pi * (value ** 3)

#Display results
print(f"The area of the square is : {area_square}")
print(f"The area of the circle is: {area_circle}")
print(f"The volume of the cube is : {volume_cube}")
print(f"The volume of the sphere is: {voume_sphere}")

print()
#Stretch 3: cm -> m conversion

#Area of square
side = float(input('What is the length of a side of the square (in cm)? '))
area_of_square = side ** 2
print(f"The area of the square is : {area_of_square} cm^2")
print(f"The area of the square is : {area_of_square / 10000} m^2")

#Area of a rectangle
length = float(input('What is the length of rectangle  (in cm)? '))
width = float(input('What is the width of the rectangle  (in cm)? '))
area_of_rectangle = length * width
print(f"The area of the rectangle is : {area_of_rectangle} cm^2")
print(f"The area of the rectangle is : {area_of_rectangle / 10000} m^2")

#Area of a circle
radius = float(input('What is the radius of the circle  (in cm)? '))
area_of_circle = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area_of_circle} cm^2")
print(f"The area of the circle is: {area_of_circle / 10000} m^2")