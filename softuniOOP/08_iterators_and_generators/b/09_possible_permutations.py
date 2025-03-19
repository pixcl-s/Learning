# Create a generator function called possible_permutations() which should receive a list and return lists with
# all possible permutations between its elements.
from itertools import permutations
from typing import List


def possible_permutations(stuff: List[int]) -> List[int]:
    x = (list(y) for y in permutations(stuff))

    yield from x


# test
[print(n) for n in possible_permutations([1, 2, 3])]
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

print()

# test
[print(n) for n in possible_permutations([1])]
# output
# [1]
