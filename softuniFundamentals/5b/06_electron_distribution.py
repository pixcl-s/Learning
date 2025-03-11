
# You will receive a single integer - the number of electrons.
# Your task is to fill shells until there are no more electrons left.
# The rules for electron distribution are as follows:
# The maximum number of electrons in a shell can be 2*n^2, where n is the position of a shell (starting from 1).
# For example, the maximum number of electrons in the 3rd shield can be 2*3^2 = 18.
# You should start filling the shells from the first one at the first position.
# If the electrons are enough to fill the first shell,
# the left unoccupied electrons should fill the following shell and so on.
# In the end, print a list with the filled shells.

electrons = int(input())

huh = []
iteration = 1

while electrons > 0:
    electro = 2*iteration**2

    if electrons >= electro:
        huh.append(electro)
    elif electrons < electro:
        huh.append(electrons)

    electrons -= electro
    iteration += 1

print(huh)
