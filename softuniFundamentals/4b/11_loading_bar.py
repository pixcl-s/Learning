
# You will receive a single integer number between 0 and 100  (inclusive) divisible by 10
# without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.

def percentages(digit):
    percent = digit // 10
    return percent


def dot(digit):
    dot = 10 - percentages(number)
    return dot


number = int(input())

percents = percentages(number)
dots = dot(number)

if number == 100:
    print("100% Complete! \n[%%%%%%%%%%]")
else:
    print(f"{number}% " + "[" + ("%" * percents) + ("." * dots) + "]""\nStill loading...")
