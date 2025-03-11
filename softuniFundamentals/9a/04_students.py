
# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}"
# On the last line, you will receive the name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course
# in the format: "{name} - {ID}" on separate lines.

school = {}
looking_for = ""

while True:
    students = input()
    if ":" not in students:
        looking_for = students.replace("_", " ")

        break

    students = students.split(":")
    if students[2] not in school:
        school[students[2]] = []
    school[students[2]].append(f"{students[0]}-{students[1]}")

to_print = school[looking_for]
for x in to_print:
    print(x.replace("-", " - "))
