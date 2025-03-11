#
# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = float(input())

if marks <= 25:
    print("Your grade is F DUMASS")
elif marks <= 45:
    print("Your grade is E less of a DUMASS")
elif marks <= 50:
    print("Your grade is D not a DUMASS")
elif marks <= 60:
    print("Your grade is C")
elif marks <= 80:
    print("Your grade is B good shit")
elif marks > 80:
    print("Your grade is A LEZ GO")
