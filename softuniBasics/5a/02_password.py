
# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
# ⦁	при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# ⦁	при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

username = input("Username: ")
password = input("Password: ")

enter_password = input("Enter Password: ")

while enter_password != password:
    enter_password = input("Wrong password, try again: ")

if enter_password == password:
    print(f"Welcome {username}!")
