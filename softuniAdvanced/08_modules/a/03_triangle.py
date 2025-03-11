# Create a module for printing a triangle. You will receive an integer number which is the size of the triangle.
# input         output
# 3             1
#               1 2
#               1 2 3
#               1 2
#               1

from my_modules import triangle_module

triangle_size = int(input())

triangle_module.triangle(triangle_size)
