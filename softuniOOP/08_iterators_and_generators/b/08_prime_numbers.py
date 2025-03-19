# Create a generator function called get_primes() which should receive a list of integer numbers and return a list
# containing only the prime numbers from the initial list.
from typing import List


def get_primes(digits: List[int]) -> List[int]:
    for x in digits:
        if x <= 1:
            continue
        for y in range(2, x):
            hm = x / y
            if "0" in str(hm) and len(str(hm)) == 3:
                break
        else:
            yield x


# test
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
# output
# [2, 3, 5]

print()

# test
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
# output
# []
