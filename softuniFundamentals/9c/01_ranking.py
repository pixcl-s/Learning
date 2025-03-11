
# Here comes the final and the most interesting part – the Final ranking of the candidate-interns.
# The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni.
# Here is your final task.
# You will receive some lines of input in the format
# "{contest}:{password for contest}"
# until you receive "end of contests".
# Save that data because you will need it later.
# After that you will receive another type of input in the format
# "{contest}=>{password}=>{username}=>{points}"
# until you receive "end of submissions". Here is what you need to do.
# Check if the contest is valid (It is considered valid if you received it in the first type of input)
# Check if the password is correct for the given contest
# If the contest and the password are valid,
# save the user with the contest they take part in (a user can take part in many contests)
# and the points the user has in the given contest.
# If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points
# (total points for all contents they participated in) in the format
# "Best candidate is {user} with total {total_points} points.".
# After that print all students ordered by their names.
# For each user print each contest with the points in descending order. See the examples.
# Input
# Strings in format "{contest}:{password for contest}" until the "end of contests" command.
# There will be no case with two equal contests
# Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# There will be no case with 2 or more users with the same total points!
# Output
# On the first line, print the best user in the format "Best candidate is {user} with total {total points} points.".
# Then print all students ordered as mentioned above in the format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"
# Constraints
# The strings may contain any ASCII character except from (:, =, >).
# The numbers will be in range [0 - 10000].
# Second input is always valid.


def best_student(subs):
    points = 0
    student = ""
    for stud, dictionarie in subs.items():
        if sum(dictionarie.values()) > points:
            points = sum(dictionarie.values())
            student = stud

    return points, student


contests = {}
submissions = {}

while True:
    the_input = input()
    if the_input == "end of contests":
        break
    contest, password = the_input.split(":")

    if contest not in contests:
        contests[contest] = password

while True:
    da_input = input()
    if da_input == "end of submissions":
        break
    contes, password, person, point = da_input.split("=>")
    point = int(point)
    if contes in contests:
        if contests[contes] == password:
            if person not in submissions:
                submissions[person] = {}
            if contes not in submissions[person]:
                submissions[person][contes] = 0
            if submissions[person][contes] < point:
                submissions[person][contes] = point

poin_ts, stude_nt = best_student(submissions)

print(f"Best candidate is {stude_nt} with total {poin_ts} points.")
print("Ranking:")

huh = list(submissions.keys())
huh.sort()
sorted_submissions = {a: submissions[a] for a in huh}

for x, y in sorted_submissions.items():
    print(x)
    another_sorting = {key: value for key, value in sorted(y.items(), key=lambda num: num)}
    for z, w in another_sorting.items():
        print(f"#  {z} -> {w}")