
# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.


a_string = input()
how_many_times = int(input())

end_result = lambda a, b: a * b

print(end_result(a_string, how_many_times))
