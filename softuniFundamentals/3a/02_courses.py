
# On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

courses = []

number_of_courses = int(input())

for _ in range(number_of_courses):
    course = input()
    courses.append(course)

print(courses)
