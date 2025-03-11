# Write a program that finds the smallest subset of sets, which contains all elements from a given sequence.
# In the Set Cover problem, we are given two sets - a set of sets (we'll call it sets) and a universe (a sequence).
# The sets contain all elements from the universe and no others, however, some elements are repeated.
# The task is to find the smallest subset of sets that contains all elements in the universe.
# Input
# · On the first line, you will receive the universe.
# · On the second line, you will receive the target number of sets.
# · On the next lines, you will receive different sets of sets.
# input             output
# 1, 2, 3, 4, 5     Sets to take (4):
# 4                 { 2, 4 }
# 1                 { 1 }
# 2, 4              { 5 }
# 5                 { 3 }
# 3

universe = set(input().split(", "))
sets_of_sets = []
for _ in range(int(input())):
    a_set = set(input().split(", "))
    print(a_set)
    sets_of_sets.append(set(a_set))

print(sets_of_sets)
