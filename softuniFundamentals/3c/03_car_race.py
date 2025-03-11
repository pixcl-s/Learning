
# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers.
# Each number represents the time the car needs to pass through that step (the index).
# There will be two cars. The first one starts from the left side, and the other one starts from the right side.
# The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time
# (the racer with less time). If you have a zero in the list,
# you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

race_track = input().split()

left_racer_time = 0
right_racer_time = 0

for i in range(len(race_track) // 2):
    race_track.reverse()
    right_racer_time += int(race_track[i])
    if int(race_track[i]) == 0:
        right_racer_time -= right_racer_time * 0.20

    race_track.reverse()
    left_racer_time += int(race_track[i])
    if int(race_track[i]) == 0:
        left_racer_time -= left_racer_time * 0.20

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")

