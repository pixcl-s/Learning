
# On the first line, you will receive a number n.
# On the following n lines, you will receive integers. You should create and print two lists:
# ⦁	One with all the positive (including 0) numbers
# ⦁	One with all the negative numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

positive = []
negative = []

count_positives = 0
sum_of_negatives = 0

how_many = int(input())

for _ in range(how_many):
    number = int(input())

    if number >= 0:
        positive.append(number)
        count_positives += 1
    else:
        negative.append(number)
        sum_of_negatives += number

print(positive)
print(negative)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
