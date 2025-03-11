
# Да се напише програма, в която потребителят въвежда вида и
# размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида:
# квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).
# ⦁	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# ⦁	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# ⦁	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# ⦁	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.

from math import pi

figure = input("square, rectangle, circle, triangle: ")

if figure == "square":
    length = float(input())
    area_of_square = length * length
    print(f"{area_of_square:.3f}")
elif figure == "rectangle":
    length_a = float(input())
    length_b = float(input())
    area_of_rectangle = length_a * length_b
    print(f"{area_of_rectangle:.3f}")
elif figure == "circle":
    radius = float(input())
    area_of_circle = pi * (radius * radius)
    print(f"{area_of_circle:.3f}")
elif figure == "triangle":
    length = float(input())
    height = float(input())
    area_of_triangle = 1/2 * length * height
    print(f"{area_of_triangle:.3f}")


