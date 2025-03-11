
# За лятната ваканция в списъка със задължителна литература на Жоро
# има определен брой книги. Понеже Жоро предпочита да играе с приятели навън,
# вашата задача е да му помогнете да изчисли колко часа на ден трябва да отделя,
# за да прочете необходимата литература.

pages = int(input())
page_per_hour = int(input())
days_to_read = int(input())

hours_per_book = pages / page_per_hour
hours_per_day = int(hours_per_book / days_to_read)

print(hours_per_day)