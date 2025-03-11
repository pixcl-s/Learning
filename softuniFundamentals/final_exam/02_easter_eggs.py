# You will be given a text string.
# To find the hidden eggs and their amount, read them and mark the ones that are valid, considering the following rules:
# ⦁	Eggs' color:
# ⦁	Surrounded by one or more "@" or "#" (they don't have to be the same).
# ⦁	It is written with lower case alphabetical letters only.
# ⦁	Each color should be minimum 3 letters long.
# ⦁	Amount:
# ⦁	Always positioned after the color.
# ⦁	Between the color and the amount there could or could not be any other characters.
# If there are, they must NOT be alphabetical letters or digits. Otherwise, the color-amount combination is invalid.
# ⦁	Surrounded by one or more "/".
# ⦁	Contains only digits.
# ⦁	If the color or the amount is not valid, we consider that the color-amount combination is invalid.
# Examples of valid eggs: @red@*/54/, #green##//2//, @@@yellow#@*/%^&/36/, @#blue@*/1//
# Examples of invalid eggs: ##@InvalidColor##/54/, @notc0l0r@*23*, @invalid_color@/notnumber/
# Next, you will have to print all the valid eggs like following:
# "You found {amount} {color} eggs!" for every color-amount combination.
import re

eggs = input()
pattern = r"[@|#]+([a-z]{3,})[@|#]+\W*\/+(\d+)\/+"

valid_eggs = re.findall(pattern, eggs)

for x in valid_eggs:
    print(f"You found {x[1]} {x[0]} eggs!")
