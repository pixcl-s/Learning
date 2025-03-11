
# You will be receiving lines in the following format:
# "{username}-{language}-{points}" until you receive "exam finished".
# You should store each username and their submissions and points.
# If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format:
# "{username}-banned"
# In that case, you should remove the user from the contest but preserve his submissions
# in the total count of submissions for each language.
# After receiving the "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format:
# "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# ⦁	Print the exam results for each participant
# ⦁	After that, print each language in the format shown above
# ⦁	Allowed working time / memory: 100ms / 16MB

students = {}
courses = {}

while True:
    the_input = input()
    if the_input == "exam finished":
        break
    if "banned" in the_input:
        user = the_input.split("-")
        del students[user[0]]
        continue

    user, course, points = the_input.split("-")

    if course not in courses:
        courses[course] = 1
    else:
        courses[course] += 1

    if user not in students:
        students[user] = 0

    if students[user] < int(points):
        students[user] = int(points)

print("Results:")
for student, point in students.items():
    print(f"{student} | {point}")

print("Submissions:")
for cours, subs in courses.items():
    print(f"{cours} - {subs}")
