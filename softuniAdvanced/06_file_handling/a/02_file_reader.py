# You are given a file called numbers.txt with the following content:
# 1
# 2
# 3
# 4
# 5
# Create a program that reads the numbers from the file.Print on the console the sum of those numbers.

file = open("txt_files/numbers.txt")

sumage = 0

for x in file.readlines():
    sumage += int(x)

print(sumage)

