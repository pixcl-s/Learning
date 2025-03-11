
# Write a function that, depending on the first line of the input,
# reads one of the following strings:"int","real", or "string".
# If the data type is an int, multiply the number by 2.
# If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# If the data type is a string, surround the input with "$".
# Print the result on the console.


# def integer(digit):
#     return print(int(digit) * 2)
#
#
# def real(digit):
#     return print(f"{int(digit) * 1.5:.2f}")
#
#
# def string(digit):
#     return print(f"${digit}$")
#
#
# command = input()
#
# if command == "int":
#     integer(input_)
# elif command == "real":
#     real(input_)
# elif command == "string":
#     string(input_)

command = input()

if command == "int":
    input_one = int(input())
    print(input_one * 2)
elif command == "real":
    input_two = float(input())
    print(f"{input_two * 1.5:.2f}")
elif command == "string":
    input_three = input()
    print(f"${input_three}$")

