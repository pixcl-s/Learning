
# Help plan the next Programming Fundamentals course by keeping track of the lessons
# that will be included in the course and all the exercises for the lessons.
# Before the course starts, there are some changes to be made.
# On the first input line, you will receive the initial schedule of lessons
# and exercises that will be part of the next course,
# separated by a comma and a space ", ".
# Until you receive the "course start" command, you will be given some commands to modify the course schedule.
# The possible commands are:

# "Add:{lessonTitle}" - add the lesson to the end of the schedule if it does not exist.
# "Insert:{lessonTitle}:{index}" - insert the lesson to the given index, if it does not exist.
# "Remove:{lessonTitle}" - remove the lesson, if it exists.
# "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons if they exist.
# "Exercise:{lessonTitle}" - add Exercise in the schedule right after the lesson index,
# if the lesson exists and there is no exercise already,
# in the following format "{lessonTitle}-Exercise".
# If the lesson doesn't exist, add the lesson at the end of the course schedule, followed by the Exercise.

# Note: Each time you Swap or Remove a lesson,
# you should do the same with the Exercises, if there are any following the lessons.

# Input / Constraints
# On the first line - the initial schedule lessons - strings, separated by comma and space ", ".
# Until "course start" you will receive commands in the format described above.
# Output
# Print the whole course schedule, each lesson on a new line with its number (index) in the schedule:
# "{lesson index}.{lessonTitle}".

courses = input().split(", ")

while True:
    commands = input()

    if commands == "course start":
        break

    commands = commands.split(":")

    if commands[0] == "Add":
        if commands[1] not in courses:
            courses.append(commands[1])
    elif commands[0] == "Insert":
        if commands[1] not in courses:
            courses.insert(int(commands[2]), commands[1])
    elif commands[0] == "Remove":
        if commands[1] in courses:
            courses.remove(commands[1])
        if f"{commands[1]}-Exercise" in courses:
            courses.remove(f"{commands[1]}-Exercise")
    elif commands[0] == "Swap":
        indeks_one = courses.index(commands[1])
        indeks_two = courses.index(commands[2])
        if commands[1] in courses and commands[2] in courses:
            courses[indeks_one], courses[indeks_two] = courses[indeks_two], courses[indeks_one]
        if f"{commands[1]}-Exercise" in courses:
            courses.remove(f"{commands[1]}-Exercise")
            courses.insert(indeks_two + 1, f"{commands[1]}-Exercise")
        if f"{commands[2]}-Exercise" in courses:
            courses.remove(f"{commands[2]}-Exercise")
            courses.insert(indeks_one + 1, f"{commands[2]}-Exercise")
    elif commands[0] == "Exercise":
        if f"{commands[1]}-Exercise" in courses:
            continue
        elif commands[1] in courses:
            location = courses.index(commands[1])
            courses.insert(location, f"{commands[1]}-Exercise")
        elif commands[1] not in courses:
            courses.append(commands[1])
            courses.append(f"{commands[1]}-Exercise")

for x in range(len(courses)):
    print(f"{x + 1}.{courses[x]}")
