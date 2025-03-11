
# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and grade.
# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point in the format:
# "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

students = {}

for _ in range(int(input())):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = []

    students[student].append(grade)

# for person, grades in students.items():
#     average_grade = sum(float(x) for x in grades) / len(grades)
#     print(f"{person} -> {' '.join(grades)} (avg: {average_grade:.2f})")

for person, digit in students.items():
    avrg = sum(digit) / len(digit)
    formated = [str(f"{nut:.2f}") for nut in digit]
    print(f"{person} -> {' '.join(formated)} (avg: {avrg:.2f})")

# 100/100
