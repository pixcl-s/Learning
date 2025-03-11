# Create a function named list_roman_emperors that receives information about various Roman emperors, their success status, and their rule length and returns a sorted result as one formatted string.
# It will receive an unknown number of arguments (tuples) and keyword arguments (key-value pairs). See the examples below.
# The arguments will be passed as follows:
# · The first group of arguments will contain an unknown number of tuples with two elements
# o The first element represents the Roman emperor's name (a valid string)
# o The second element represents the success status of the emperor (a Boolean value)
# · The second group will contain an unknown number of keyword arguments (key-value pairs)
# o The key will represent the name of the emperor (a valid string)
# o The value will represent the length of their rule (a positive integer)
# After receiving the data and calling the function:
# · You should check each emperor's success status (True or False) and keep the information about them in separate collections (you will have to sort them in the next steps)
# · Sort the successful emperors by the length of their rule in descending order
# o If there are emperors with the same length of rule, sort them alphabetically, in ascending order
# · Sort the unsuccessful emperors by the length of their rule in ascending order
# o If there are emperors with the same length of rule, sort them alphabetically, in ascending order
# · The first line of your output string should contain the total number of all emperors:
# o "Total number of emperors: {num_of_all_emperors}"
# · Next, arrange the sorted data under the appropriate headings:
# o For successful emperors (if any), use the heading "Successful emperors:"
# § Skip the heading if there are no successful emperors
# o For unsuccessful emperors (if any), use the heading "Unsuccessful emperors:"
# § Skip the heading if there are no unsuccessful emperors
# o Note that you may receive data either for successful or unsuccessful emperors and your output should contain sorted information for the received type only. See the examples below.
# In the end, return the output as described below.
# Note: Submit only the function in the judge system
# Output
# · The returned output should look like this (each on a new line):
# "Total number of emperors: {num_of_all_emperors}"
# "Successful emperors:"
# "****{emperor_name1}: {number_of_years}"
# "****{emperor_name2}: {number_of_years}"
# ...
# "****{emperor_nameN}: {number_of_years}"
# "Unsuccessful emperors:"
# "****{emperor_name1}: {number_of_years}"
# "****{emperor_name2}: {number_of_years}"
# ...
# "****{emperor_nameN}: {number_of_years}"
# o Prefix the name of each emperor with exactly four asterisks "****"
# o Separate the name of the emperor and his years of rule with a colon and a single space ": "
# o If you receive only one type of emperor (successful or unsuccessful), return only the type you've got. Do not include the heading for the missing type in your formatted string. See the examples below for clarification.
# Constraints
# · The arguments will always be before the keyword arguments.
# · Each tuple will always provide a unique name (a valid string) of the emperor and his status (a valid Boolean value).
# · Each keyword argument will always provide a valid emperor's name (a string that corresponds to the same emperor's name that will be in one of the tuples) and his length of rule (a positive integer).
# · You will always receive at least one tuple with the emperor's name and status and at least one valid keyword argument containing the same emperor's name as a key.

def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for x in args:
        if x[1]:
            successful_emperors[x[0]] = kwargs[x[0]]
        else:
            unsuccessful_emperors[x[0]] = kwargs[x[0]]
    to_return = f"Total number of emperors: {len(args)}\n"

    if successful_emperors:
        to_return += "Successful emperors:\n"
        successful_emperors = sorted(successful_emperors.items(), key=lambda x: (-x[1], x))
        for key, value in successful_emperors:
            to_return += f"****{key}: {value}\n"
    if unsuccessful_emperors:
        to_return += "Unsuccessful emperors:\n"
        unsuccessful_emperors = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x))
        for key, value in unsuccessful_emperors:
            to_return += f"****{key}: {value}\n"

    return to_return

# 100/100

# test
print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
