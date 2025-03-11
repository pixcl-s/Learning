#
# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

import math

classes_held = int(input())
classes_attended = int(input())

have_to_attend = math.floor(classes_held * 0.75)

percent_attended_classes = math.floor((classes_attended / classes_held) * 100)

if have_to_attend < classes_attended:
    print(f"You have attended {percent_attended_classes}% of classes")
    print("You are allowed to take exam")
else:
    print(f"You have attended {percent_attended_classes}% of classes")
    print("You are not allowed to take exam")
