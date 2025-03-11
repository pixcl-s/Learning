
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number.
# You need to keep track of every contest and points of each user:
# If the user has already participated in the contest,
# update their points only if the new ones are more than the older ones.
# Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time".
# At that point, you should print each contest in order of input,
# for each contest print the participants ordered by points in descending order,
# then ordered by name in ascending order.
# After that, you should print individual statistics for every participant ordered by
# total points in descending order, and then by alphabetical order.
# Input / Constraints
# The input comes in the form of commands in one of the formats specified above.
# Username and contest name always will be one word.
# Points will be an integer in the range [0, 1000].
# There will be no invalid input lines.
# If all sorting criteria fail, the order should be by order of input.
# The input ends when you receive the command "no more time".
# Output
# The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# After you print all contests, print the individual statistics for every participant.
# The output format is:
# "Individual standings:
# {username1} -> {total_points}
# {username} -> {total_points}
# …
# {N}. {username} -> {total_points}"

people = {}

while True:
    the_input = input()
    if the_input == "no more time":
        break
    user, contest, points = the_input.split(" -> ")
    points = int(points)

    if contest not in people:
        people[contest] = {}
    if user not in people[contest]:
        people[contest][user] = 0
    if people[contest][user] < points:
        people[contest][user] = points

person = {}

for x, y in people.items():
    print(f"{x}: {len(y)} participants")
    sortage = {key: value for key, value in sorted(y.items(), key=lambda num: num[1], reverse=True)}
    counter = 1

    for z, w in sortage.items():
        print(f"{counter}. {z} <::> {w}")
        counter += 1
        if z not in person:
            person[z] = 0
        person[z] += w

another_sortage = {key: value for key, value in sorted(person.items(), key=lambda num: num[1], reverse=True)}
another_counter = 1
print("Individual standings:")
for a, b in another_sortage.items():
    print(f"{another_counter}. {a} -> {b}")
    another_counter += 1