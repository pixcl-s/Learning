
# Take input of age of 3 people by user and determine oldest and youngest among them.

age_1 = int(input())
age_2 = int(input())
age_3 = int(input())

if age_1 > age_2:
    if age_1 > age_3:
        print ("Oldest is ", age_1)

if age_2 > age_1:
    if age_2 > age_3:
        print ("Oldest is ", age_2)

if age_3 > age_1:
    if age_3 > age_2:
        print("Oldest is ", age_3)

if age_1 < age_2:
    if age_1 < age_3:
        print ("Youngest is ", age_1)

if age_2 < age_1:
    if age_2 < age_3:
        print ("Youngest is ", age_2)

if age_3 < age_1:
    if age_3 < age_2:
        print("Youngest is ", age_3)
