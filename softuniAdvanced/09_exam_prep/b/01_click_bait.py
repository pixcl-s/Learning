# Your task is to simulate a "content optimization" process for a website using two sequences of scores and design an algorithm for a website to process user engagement on two types of content:
# · Suggested Links - processed using the FIFO principle
# · Featured Articles - processed using the LIFO principle
# You must follow specific rules to process the elements and calculate an Engagement Value, which determines if the target goal is achieved.
# Input Data
# · The first line contains space-separated integers representing the engagement scores of Suggested Links
# · The second line contains space-separated integers representing the popularity scores of Featured Articles
# · The third line contains a single integer - the Target Engagement Value
# Rules
# You should repeatedly perform the following steps until one of the sequences becomes empty:
# Take one element from each sequence:
# · Take the first element from the Suggested Links
# · Take the last element from the Featured Articles
# Compare the two elements:
# · Identify the greater element and the smaller element
# · Remember the sequence of origin of the greater element, you will need it later
# Calculations:
# · Find the remainder between the two elements. The greater element will be used as a dividend and the smaller as a divisor using a Modulo Operation
# · If the greater element is from the Featured Articles (LIFO) collection:
# o Add the remainder to the Final Feed Collection as a positive element
# o Double the remainder and return the result to the LIFO collection (at the end). If the remainder equals zero, skip this operation and proceed with the next calculation
# · If the greater element is from the Suggested Links (FIFO) collection:
# o Add the remainder to the Final Feed Collection as a negative element
# o Double the remainder and return the result to the FIFO collection (at the end). If the remainder equals zero, skip this operation and proceed with the next calculation
# · If elements are equal add zero (0) to the Final Feed Collection and do not return anything to the LIFO or FIFO collections
# After processing:
# Find the Total Engagement Value as a sum of all elements in the Final Feed Collection.
# · If the Total Engagement Value is greater than or equal to the Target Engagement Value, the goal has been achieved.
# · If the Total Engagement Value is less than the Target Engagement Value, the goal has not been achieved
# o Calculate how far short the Total Engagement Value is from the target by subtracting the Total Engagement Value from the Target Engagement Value: Shortfall = Target - Total
# Print the Final Feed collection on the Console, comma, and space separated (", "). Print the appropriate output for the engagement value on the Console.
# Output
# · Print the Final Feed Collection:
# "Final Feed: {element1}, {element2} … {elementn}"
# · Calculate the Total Engagement Value:
# o If the Total Engagement Value is greater than or equal to the target, print:
# "Goal achieved! Engagement Value: {total_engagement_value}"
# o If the Total Engagement Value is less than the target (Shortfall = Target - Total), print:
# "Goal not achieved! Short by: {shortfall}"
# Constraints
# · Always process elements in the order described
# · All of the given numbers will be valid integers in the range [1-1000]
# · Use modulo operation (%) to calculate the remainder
# · Pay attention to the sign of the remainder in the Final Feed
# · Both sequences will initially have at least one element.
# input                 output
# 45 65 35 25 70        Final Feed: -5, 0, -5, -5, -10, 5, 0
# 15 30 20 10 5 40      Goal not achieved! Short by: 75
# 55

from collections import deque

suggested_links = deque([int(x) for x in input().split()])
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())

final_feed = []

while suggested_links and featured_articles:
    link = suggested_links.popleft()
    article = featured_articles.pop()

    remainder = link % article if link > article else article % link

    if article > link:
        final_feed.append(remainder)
        if not remainder == 0:
            featured_articles.append(remainder*2)
    elif article < link:
        final_feed.append(-remainder)
        if not remainder == 0:
            suggested_links.append(remainder*2)
    elif article == link:
        final_feed.append(0)

total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join(str(x) for x in final_feed)}")
print(f"Goal achieved! Engagement Value: {total_engagement_value}" if total_engagement_value >= target_engagement_value
      else f"Goal not achieved! Short by: {target_engagement_value - total_engagement_value}")

# 100/100
