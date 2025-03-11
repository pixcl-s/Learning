
# You have an empty stack. You will receive an integer – N.
# On the following N lines, you will receive queries. Each query is one of these four types:
# '1 {number}' – push the number (integer) into the stack
# '2' – delete the number at the top of the stack
# '3' – print the maximum number in the stack
# '4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"

how_many = int(input())

stackage = []

functions = {
    "1": lambda x: stackage.append(int(x)),
    "2": lambda: stackage.pop() if stackage else None,
    "3": lambda: print(max(stackage)) if stackage else None,
    "4": lambda: print(min(stackage)) if stackage else None
}

for _ in range(how_many):
    query = input().split()
    functions[query[0]](*query[1:])

while len(stackage) > 1:
    print(stackage.pop(), end=", ")
print(stackage.pop())

# 100/100
