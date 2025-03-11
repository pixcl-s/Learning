
# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

stackage = list(input())

stack = []

for x in range(len(stackage)):
    if stackage[x] == "(":
        stack.append(x)
    elif stackage[x] == ")":
        print("".join(stackage[stack.pop():x+1]))

# 100/100
