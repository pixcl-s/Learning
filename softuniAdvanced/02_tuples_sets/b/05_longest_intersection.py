
# Write a program that finds the longest intersection. You will be given a number N.
# On each of the next N lines you will be given two ranges in the format:
# "{first_start},{first_end}-{second_start},{second_end}".
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
# Finally, you should find the longest intersection of all N intersections,
# print the numbers that are included and its length in the format:
# "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.

digits = []
intersections = []
for _ in range(int(input())):

    rotation = 1
    first_part = input().split("-")

    second_part_one = set()
    second_part_two = set()

    for x in first_part:
        start, end = x.split(",")

        for y in range(int(start), int(end) + 1):
            if rotation == 1:
                second_part_one.add(y)
            else:
                second_part_two.add(y)
        rotation += 1

    intersections.append(list(second_part_one & second_part_two))

longest = max(intersections, key=len)

print(f"Longest intersection is {longest} with length {len(longest)}")

# 100/100
