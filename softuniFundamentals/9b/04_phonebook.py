
# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling out the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format:
# "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

phonebook = {}
num = 0

while True:
    person = input()
    if "-" not in person:
        num = int(person)
        break
    name, number = person.split("-")
    phonebook[name] = number



for _ in range(num):
    lul = input()
    if lul in phonebook:
        print(f"{lul} -> {phonebook[lul]}")
    else:
        print(f"Contact {lul} does not exist.")

