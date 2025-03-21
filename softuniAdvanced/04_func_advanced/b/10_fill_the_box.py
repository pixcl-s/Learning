# Write a function called fill_the_box that receives a different number of arguments representing:
# · the height of a box
# · the length of a box
# · the width of a box
# · different numbers - each representing the quantity of cubes. Each cube has an exact size of 1 x 1 x 1
# · a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
# · There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
# · If, in the end, there is free space left in the box, print:
# o "There is free space in the box. You could put {free space in cubes} more cubes."
# · If there is no free space in the box, print:
# o "No more free space! You have {cubes left} more cubes."


def fill_the_box(height, length, width, *cubes):
    box_space = height * length * width
    left_cubes = []
    for x in cubes:
        if x == "Finish":
            break
        elif box_space > 0:
            if box_space - x < 0:
                left_cubes.append(x - box_space)
                box_space = 0
            else:
                box_space -= x
        else:
            left_cubes.append(x)
    if left_cubes:
        return f"No more free space! You have {sum(left_cubes)} more cubes."
    return f"There is free space in the box. You could put {box_space} more cubes."

# 100/100


# test
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# output
# There is free space in the box. You could put 13 more cubes.
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
