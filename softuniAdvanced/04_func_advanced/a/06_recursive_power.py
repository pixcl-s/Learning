# Create a recursive function called recursive_power() which should receive a number and a power.
# Using recursion, return the result of number ** power. Submit only the function in the judge system.
# test                              output
# print(recursive_power(2, 10))     1024

def recursive_power(num, pow):
    result = 1
    if pow == 0:
        return result
    result = num * recursive_power(num, pow-1)
    return result


print(recursive_power(2, 10))

# 100/100
