
# Ани отива до родния си град след много дълъг период извън страната.
# Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга.
# Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст).
# Докато Ани не намери любимата си книга или не провери всички книги в библиотеката,
# програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст), която тя проверява.
# Книгите в библиотеката са свършили щом получите текст "No More Books".
# ⦁	Ако не открие търсената книгата да се отпечата на два реда:
# ⦁	"The book you search is not here!"
# ⦁	"You checked {брой} books."
# ⦁	Ако открие книгата си се отпечатва един ред:
# ⦁	"You checked {брой} books and found it."

book = input().lower()

amount = 0

new_book = input().lower()

while new_book != "no more books":

    if new_book == book:
        print(f"You checked {amount} books and found it.")
        exit()
    amount += 1
    new_book = input().lower()

print(f"The book you search is not here!")
print(f"You checked {amount} books.")
