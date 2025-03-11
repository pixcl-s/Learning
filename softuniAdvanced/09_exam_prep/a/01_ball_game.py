# On the first line, you will be given a sequence of integers representing the values of strength required to kick the ball.
# In the next line, you will be given another sequence of integers representing the values of accuracy needed to direct the ball.
# Until there are strengths and accuracies available, the program continues running.
# You need to sum the last strength and the first accuracy, then compare the result:

# · If the sum of the strength and the accuracy is equal to 100, there is a goal:
# o Remove both values (the strength and the accuracy) from their sequences.
# o You should keep track of the scored goals in total:
# § Increase total scored goals by 1 (one).

# · If the sum of the strength and the accuracy is less than 100:
# o If the value of the strength is smaller than the value of the accuracy:
# § Remove the value of the strength from the sequence.
# o If the value of the strength is greater than the value of the accuracy:
# § Remove the value of the accuracy from the sequence.
# o If both values are equal (strength = accuracy):
# § Sum the strength and accuracy values (strength + accuracy).
# Return the summation result to the strength sequence (at its initial position).
# § Remove the accuracy.

# · If the sum of the strength and the accuracy is greater than 100:
# o Decrease the strength value by 10. Return it to the strength sequence (at its initial position).
# o Move the accuracy value to the end of the accuracy sequence.

# Input / Constraints
# · On the first line, you will receive integers representing the values of the strength, separated by a single space.
# · On the second line, you will receive integers representing the values of the accuracy, separated by a single space.
# · The size of the two sequences may differ.
# · All given numbers will be valid integers in the range [10 - 90] and are divisible only by 10.
# Output
# The output of your program should be printed on the Console, on separate lines, formatted according to the following rules:
# · If Paul succeeded in scoring of exactly 3 (three) goals:
# o "Paul scored a hat-trick!"
# · If Paul failed to score a single goal:
# o "Paul failed to score a single goal."
# · If Paul scored more than 3 (three) goals:
# o "Paul performed remarkably well!"
# · If Paul scored more than 0 (zero) but less than 3 (three) goals:
# o "Paul failed to make a hat-trick."
# · Finally, print the total goals scored by Paul if there are any:
# o "Goals scored: {total goals}"
# · At the end of the program
# o If there are any values in the strength sequence, print:
# § "Strength values left: {strenght1}, {strenght2}, (…),{strenghtn}"
# o If there are any values in the accuracy sequence, print:
# § "Accuracy values left: {accuracy1}, {accuracy2}, (…),{accuracyn}"
# o If there are no values in one or both sequences, skip the printing.
# input                 output
# 10 20 30 40 90        Paul scored a hat-trick!
# 20 70 20 30 60        Goals scored: 3
#                       Strength values left: 10, 20

from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque([int(x) for x in input().split()])

goals = 0

while strength and accuracy:
    strgh = strength.pop()
    acc = accuracy.popleft()
    shot_at_goal = strgh + acc

    if shot_at_goal == 100:
        goals += 1
    elif shot_at_goal < 100:
        if strgh < acc:
            accuracy.appendleft(acc)
        elif strgh > acc:
            strength.append(strgh)
        elif strgh == acc:
            strength.append(shot_at_goal)
    elif shot_at_goal > 100:
        strength.append(strgh-10)
        accuracy.append(acc)

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals > 3:
    print("Paul performed remarkably well!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")

if goals:
    print(f"Goals scored: {goals}")

if strength:
    print(f"Strength values left: {', '.join(str(x) for x in strength)}")
if accuracy:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracy)}")

# 100/100
