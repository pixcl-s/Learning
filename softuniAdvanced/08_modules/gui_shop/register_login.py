import tkinter
import json
from ui_base import start
from helpers import screen_cleaner
from shop import product_screen


def info():
    username_entry = tkinter.Entry(start)
    password_entry = tkinter.Entry(start)
    username_label = tkinter.Label(start, text="Username", bg="grey14", fg="snow")
    password_label = tkinter.Label(start, text="Password", bg="grey14", fg="snow")
    return username_entry, password_entry, username_label, password_label


def loging_in(username, password):
    with open("db/users_login.txt") as file:
        data = file.readlines()
        data = dict([x.strip().split(", ") for x in data])
        if username in data:
            for user, passwrd in data.items():
                if user == username and passwrd == password:
                    with open("db/current_user.txt", "w") as file:
                        file.write(username)
                    return product_screen()
            else:
                login_screen(error="Invalid username or password!")
        else:
            login_screen(error="User doesn't exit!")


def registering(username, password, fst, snd):
    with open("db/users_login.txt") as file:
        data = file.readlines()
        data = dict([x.strip().split(", ") for x in data])
        if username in data:
            return register_screen(error="Username already exist!")

    with open("db/users_login.txt", "a") as file:
        file.writelines(f"\n{username}, {password}")

    with open("db/users_information.txt", "a") as file:
        file.write("\n")
        file.writelines(json.dumps({"username": username, "password": password,
                                    "first_name": fst, "last_name": snd, "products": []}))

    login_screen()


def login_screen(error=None):
    screen_cleaner()
    username_entry, password_entry, username_label, password_label = info()

    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)

    enter_button = tkinter.Button(start, text="Enter",
                                  command=lambda: loging_in(username_entry.get().strip(), password_entry.get().strip()))
    enter_button.grid(row=2, column=1)

    if error:
        tkinter.Label(start, text=error, bg="grey14", fg="snow").grid(row=3, column=0, columnspan=2)


def register_screen(error=None):
    screen_cleaner()
    username_entry, password_entry, username_label, password_label = info()

    first_name_label = tkinter.Label(start, text="First Name")
    first_name_label.grid(row=0, column=0)
    first_name_entry = tkinter.Entry(start)
    first_name_entry.grid(row=0, column=1)

    last_name_label = tkinter.Label(start, text="Last Name")
    last_name_label.grid(row=1, column=0)
    last_name_entry = tkinter.Entry(start)
    last_name_entry.grid(row=1, column=1)

    username_label.grid(row=2, column=0)
    username_entry.grid(row=2, column=1)

    password_label.grid(row=3, column=0)
    password_entry.grid(row=3, column=1)

    enter_button = tkinter.Button(start, text="Enter",
                                  command=lambda: registering(username_entry.get(), password_entry.get(),
                                                              first_name_entry.get(), last_name_entry.get()))
    enter_button.grid(row=4, column=1)

    if error:
        tkinter.Label(start, text=error, bg="grey14", fg="snow").grid(row=3, column=1)


def login_register():
    frame = tkinter.Frame(start)
    frame.grid(padx=270, pady=170)
    login = tkinter.Button(frame, text="Login", bg="grey", fg="white", command=login_screen)
    login.grid(row=0, column=0, sticky="ew")
    register = tkinter.Button(frame, text="Register", bg="indigo", fg="white", command=register_screen)
    register.grid(row=1, column=0)
