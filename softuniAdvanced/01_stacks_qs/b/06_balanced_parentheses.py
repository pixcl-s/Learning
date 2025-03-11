
# You will be given a sequence consisting of parentheses.
# Your job is to determine whether the expression is balanced.
# A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis
# that occurs after the former. There will be no interval symbols between the parentheses.
# You will be given three types of parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced
# Output
# For each test case, print on a new line "YES" if the parentheses are balanced.
# Otherwise, print "NO"

from collections import deque

parentheses = deque(input())
a_stack = []

dictionary = {
    "(": ")",
    "{": "}",
    "[": "]"
}
while parentheses:
    symbol = parentheses.popleft()
    if symbol in dictionary.keys():
        a_stack.append(symbol)
    else:
        if a_stack and dictionary[a_stack[-1]] == symbol:
            a_stack.pop()
        else:
            print("NO")
            exit()

print("YES")

# 100/100
