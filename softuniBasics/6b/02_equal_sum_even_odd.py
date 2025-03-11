
# Напишете програма, която чете от конзолата две шестцифрени цели числа.
# Винаги първото въведено число ще бъде по-малко от второто.
# На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа,
# които се намират между двете, прочетени от конзолата числа и
# отговарят на условието сумата от цифрите на четни и нечетни позиции да са равни.
# Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.

first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    not_number = str(number)
    even = 0
    odd = 0
    for index, digit in enumerate(not_number):
        if index % 2 == 0:
            odd += int(digit)
        else:
            even += int(digit)

    if even == odd:
        print(number, end=" ")
