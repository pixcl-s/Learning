
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# "We have a perfect number!" - if the number is perfect.
# "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def divisors(the_number):
    positive_divisors = []

    for digit in range(1, number):
        if number % digit == 0:
            positive_divisors.append(digit)
    return sum(positive_divisors)


number = int(input())

divisor_sum = divisors(number)

if number == divisor_sum:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

