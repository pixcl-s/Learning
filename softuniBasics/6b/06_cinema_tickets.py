
# Вашата задача е да напишете програма,
# която да изчислява процента на билетите за всеки тип от продадените билети:
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции.
# Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.

# Входът е поредица от цели числа и текст:
# ⦁	На първия ред до получаване на командата "Finish" - име на филма – текст
# ⦁	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# ⦁	За всеки филм, се чете по един ред до изчерпване на свободните места в
# залата или до получаване на командата "End":
# ⦁	Типа на закупения билет - текст ("student", "standard", "kid")

# На конзолата трябва да се печатат следните редове:
# ⦁	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# ⦁	При получаване на командата "Finish" да се отпечатат четири реда:
# ⦁	"Total tickets: {общият брой закупени билети за всички филми}"
# ⦁	"{процент на студентските билети}% student tickets."
# ⦁	"{процент на стандартните билети}% standard tickets."
# ⦁	"{процент на детските билети}% kids tickets."

movie = input()


seats_taken = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != "Finish":
    seats = int(input())

    seats_taken_for_movie = 0
    for _ in range(seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
            seats_taken_for_movie += 1
            seats_taken += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            seats_taken_for_movie += 1
            seats_taken += 1
        else:
            kid_tickets += 1
            seats_taken_for_movie += 1
            seats_taken += 1

    print(f"{movie} - {((seats_taken_for_movie / seats) * 100):.2f}% full.")

    movie = input()

print(f"Total tickets: {seats_taken}")
print(f"{(student_tickets / seats_taken * 100):.2f}% student tickets.")
print(f"{(standard_tickets / seats_taken * 100):.2f}% standard tickets.")
print(f"{(kid_tickets / seats_taken * 100):.2f}% kids tickets.")
