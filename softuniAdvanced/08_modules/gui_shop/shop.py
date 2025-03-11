import tkinter
import json
import os
from helpers import screen_cleaner
from ui_base import start
from PIL import Image, ImageTk

file_path = os.path.dirname(__name__)
buy_button = None
the_buttons = []


def buying(index, product, inventory, label_qnt):
    product["quantity"] -= 1
    inventory[index] = product

    with open("db/current_user.txt") as file:
        logged_in_user = file.read()

    with open("db/users_information.txt") as file:
        users = [json.loads(x) for x in file]

    for i, x in enumerate(users):
        if logged_in_user == x["username"]:
            x["products"].append(product["name"])
            users[i] = x

    with open("db/products.txt", "w") as file:
        for x in inventory:
            file.write(json.dumps(x))
            file.write("\n")

    with open("db/users_information.txt", "w") as file:
        for x in users:
            file.write(json.dumps(x))
            file.write("\n")

    label_qnt.config(text=f"Available: {product['quantity']}", bg="grey14", fg="whitesmoke")
    if product["quantity"] == 0:
        the_buttons[index].config(tkinter.Label(text="Out Of Stock"))


def framing(index):
    frame = tkinter.Frame(start)
    frame.grid(row=0, column=index, padx=5, pady=5)
    return frame


def product_screen():
    screen_cleaner()

    with open("db/products.txt") as file:
        products = [json.loads(x) for x in file]

    for i, x in enumerate(products):
        frame = framing(i)

        label_name = tkinter.Label(frame, text=x["name"], bg="grey14", fg="ghostwhite")
        label_name.grid(row=0, column=0, sticky="ew")

        image = Image.open(os.path.join(file_path, "db/pngs", x["img_path"])).resize((110, 150))
        photo_image = ImageTk.PhotoImage(image)
        image_label = tkinter.Label(frame, image=photo_image)
        image_label.image = photo_image
        image_label.grid(row=1, column=0)

        label_quantity = tkinter.Label(frame, text=f"Available: {x['quantity']}", bg="grey14", fg="whitesmoke")
        label_quantity.grid(row=2, column=0, sticky="ew")

        global buy_button
        buy_button = tkinter.Button(frame, text="Buy", fg="black",
                                    command=lambda lblq=label_quantity, ind=i, prdct=x, prdcts=products:
                                    buying(ind, prdct, prdcts, lblq))

        buy_button.grid(row=3, column=0, sticky="ew")

        the_buttons.append(buy_button)


