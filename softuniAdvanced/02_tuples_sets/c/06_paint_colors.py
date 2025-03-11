# Write a program that finds colors in a string.
# You will be given a string on a single line containing substrings (separated by a single space)
# from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of
# the above colors' names. If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed
# for its creation could be formed from the given substrings:
# · orange = red + yellow
# · purple = red + blue
# · green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings.
# Otherwise, you should remove the last character of each substring and return them
# in the middle of the original string. If the string contains an odd number of substrings,
# you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye"
# you could not form a color with the substring "re" and "bye",
# so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
# · Single line string.
# Output
# · The list with the collected colors.
# Constraints
# · You will not receive an empty string.
# · Please consider only the colors mentioned above.
# · There won't be any cases with repeating colors.
#     Input                                                          Output
# d yel blu e low redd                                     ['yellow', 'blue', 'red']

from collections import deque


def color_check(col, look, col_two=None):
    if col in look:
        return col
    elif col_two in look:
        return col_two
    else:
        return False


not_colors = deque(input().split())

looking_for = ["red", "yellow", "blue", "orange", "purple", "green"]
secondary_colors = ["orange", "purple", "green"]
looking_for_secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

colors_found = []
waiting_room = {}

while not_colors:
    if len(not_colors) == 1:
        color = not_colors.pop()
        color_two = None
    else:
        first_part = not_colors.popleft()
        second_part = not_colors.pop()
        color = first_part + second_part
        color_two = second_part + first_part

    the_color = color_check(color, looking_for, color_two)
    if the_color in secondary_colors:
        if the_color not in waiting_room:
            waiting_room[the_color] = []
        waiting_room[the_color].append(len(colors_found))
    elif the_color:
        colors_found.append(the_color)
    elif not the_color and len(not_colors) > 1:
        # index_to_inset = len(not_colors) // 2
        if first_part[:-1]:
            not_colors.insert(len(not_colors) // 2, first_part[:-1])
            # index_to_inset += 1
        if second_part[:-1]:
            not_colors.insert(len(not_colors) // 2, second_part[:-1])

for colour, indexes in waiting_room.items():
    search_one, search_two = looking_for_secondary_colors[colour]
    if search_one in colors_found and search_two in colors_found:
        for z in indexes:
            colors_found.insert(z, colour)
print(colors_found)

# 50/100