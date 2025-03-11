
# Write a program that:
# Reads an input string
# Reverses it using a stack
# Prints the result back on the console
# Examples
# Input	                        Output
# I Love Python         	nohtyP evoL I
# Stacks and Queues	      seueuQ dna skcatS

the_stack = list(input())

while the_stack:
    print(the_stack.pop(), end="")

# 100/100
