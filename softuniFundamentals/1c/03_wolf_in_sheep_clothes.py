
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    4      3            2      1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep".
# Otherwise, return
# "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
# Input
# The input will be a single string containing the animals separated by a comma and a single space ", "
# Examples
# Input	Output
# sheep, sheep, wolf	Please go away and stop eating my sheep
# wolf, sheep, sheep, sheep, sheep, sheep	Oi! Sheep number 5! You are about to be eaten by a wolf!


herd = input().split(", ")

if herd[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    sheep_in_danger = (herd.index("wolf") + 1) - len(herd)
    print(f"Oi! Sheep number {abs(sheep_in_danger)}! You are about to be eaten by a wolf!")


