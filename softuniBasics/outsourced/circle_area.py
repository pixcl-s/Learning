#
# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi

radius = float(input())

area = pi * (radius * radius)

print(area)



# # Import the 'pi' constant from the 'math' module to calculate the area of a circle
# from math import pi
#
# # Prompt the user to input the radius of the circle
# r = float(input("Input the radius of the circle : "))
#
# # Calculate the area of the circle using the formula: area = π * r^2
# area = pi * r ** 2
#
# # Display the result, including the radius and calculated area
# print("The area of the circle with radius " + str(r) + " is: " + str(area))