import tkinter as tk
from time import sleep

import requests
from io import BytesIO

import helpers
import interface_populating
from cards_info import card_info, each_card_variant
import list_of_cards
from helpers import screen_cleaner, searching_card_to_add
import interface
from math import ceil
from PIL import Image, ImageTk

card_info = card_info


def remove_cards():
    card_to_remove = list_of_cards.list_of_cards_frame.list.curselection()[0]
    all_the_cards = list_of_cards.list_of_cards_frame.list.get(0, tk.END)[card_to_remove]
    # listbox.get(listbox.curselection())

    del card_info[all_the_cards]

    card_links = [x['uri'] for x in card_info.values()]

    list_of_cards.list_of_cards_frame.list.delete(card_to_remove)
    screen_cleaner()
    interface_populating.interface_population(card_info)

    with open("my_cards.txt", "w") as file:
        file.writelines("\n".join(card_links))


#


CARDS_PER_FRAME = 3
all_images = []


def add_card():
    new_window = tk.Toplevel(bg="grey42")

    new_window.minsize(width=500, height=300)

    the_card = searching_card_to_add(new_window)

    frames = []
    each_variant, amount = each_card_variant(the_card)
    each_variant_png = list(each_variant.keys())
    each_variant_uri = list(each_variant.values())

    for _ in range(ceil(amount / CARDS_PER_FRAME)):
        frame = tk.Frame(new_window, bg="grey22")
        frame.pack(fill=tk.BOTH, expand=True)
        frames.append(frame)

    indexes = 0

    for x in frames:
        for _ in range(CARDS_PER_FRAME):
            if indexes == len(each_variant_png):
                break

            current_img = each_variant_png[indexes]
            response_img = requests.get(current_img)
            img_data = response_img.content

            img_resize = Image.open(BytesIO(img_data)).resize((162, 227))
            img = ImageTk.PhotoImage(img_resize)
            all_images.append(img)

            card_button = tk.Button(x, image=img, bd=5, bg="grey22",
                                    command=lambda i=indexes: helpers.saving_the_card(each_variant_uri[i]))
            card_button.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
            indexes += 1
            sleep(0.5)
