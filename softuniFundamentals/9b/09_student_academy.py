
# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and
# keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

how_many = int(input())
school = {}

for _ in range(how_many):
    student = input()
    grade = float(input())

    if student not in school:
        school[student] = []
    school[student].append(grade)

exclude = []
for x in school:
    average_grade = sum(school[x]) / len(school[x])

    if average_grade < 4.50:
        exclude.append(x)
        continue
    else:
        print(f"{x} -> {average_grade:.2f}")

for z in exclude:
    if z in school:
        del school[z]