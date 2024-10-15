# Exercise 2: Calculate the Area of a Circle
# Description:
# Write a Python program that calculates the area of a circle based on user input for the radius.

import math  # Import math module to use math.pi

# Step 1: Ask for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Step 2: Calculate the area of the circle
area = math.pi * radius ** 2

# Step 3: Display the result formatted to 2 decimal places
print(f"The area of the circle with radius {radius} is: {area:.2f}")
