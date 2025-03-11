
# You will be given the coordinates of two points on a
# Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
# Write a function that prints the point which is closest to the center
# of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one.
# The resulting coordinates must be formatted to the lower integer.

from math import floor


def closest(digit1, digit2):
    closest_coordinate = 0
    if abs(digit1) < abs(digit2):
        closest_coordinate = digit1
    elif abs(digit1) > abs(digit2):
        closest_coordinate = digit2
    else:
        closest_coordinate = digit1
    return closest_coordinate


def printing(x, y):
    print(f"({x}, {y})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

coordinate_x = floor(closest(x1, x2))
coordinate_y = floor(closest(y1, y2))

printing(coordinate_x, coordinate_y)
