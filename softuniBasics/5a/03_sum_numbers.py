
# Напишете програма, която чете цяло число от конзолата и
# на всеки следващ ред цели числа, докато тяхната сума стане по-голяма или
# равна на първоначалното число. След приключване на четенето да се отпечата сумата на въведените числа

number = int(input())

sum = 0

while sum < number:
    new_number = int(input())
    sum += new_number

print(sum)
