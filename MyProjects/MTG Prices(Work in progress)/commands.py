import tkinter as tk
from time import sleep
import requests
from io import BytesIO
import interface_populating
from cards_info import card_info, each_card_variant
import list_of_cards
import helpers
from math import ceil
from PIL import Image, ImageTk
import cards_frame


cards = card_info
widget_keys_img = ["image", "bg", "width", "height"]
widget_keys_prices = ["bg", "fg", "text", "font", "cursor", "relief"]

def remove_cards():
    card_to_remove = list_of_cards.list_of_cards_frame.list.curselection()[0]
    all_the_cards = list_of_cards.list_of_cards_frame.list.get(0, tk.END)[card_to_remove]
    # listbox.get(listbox.curselection())

    all_widgets = []

    images_one = cards_frame.card_frame_one.frame.winfo_children()
    prices_one = cards_frame.card_label_one.frame.frame_in_frame.winfo_children()

    images_two = cards_frame.card_frame_two.frame.winfo_children()
    prices_two = cards_frame.card_label_two.frame.frame_in_frame.winfo_children()

    for x in range(len(images_one) // 2):
        combination_one = []
        combination_two = []

        combination_one.extend(images_one[:2])
        combination_one.extend(prices_one[:2])
        del images_one[:2], prices_one[:2]
        if len(images_two) != 0:
            combination_two.extend(images_two[:2])
            combination_two.extend(prices_two[:2])
            del images_two[:2], prices_two[:2]

        all_widgets.append(combination_one)
        if combination_two:
            all_widgets.append(combination_two)

    widgets_replacing = all_widgets[card_to_remove:]
    card_widgets_to_remove = all_widgets[-1]

    for i, y in enumerate(card_widgets_to_remove):
        y.configure(all_widgets[-1][i])
        a=6

    del cards[all_the_cards]

    card_links = [x['uri'] for x in cards.values()]

    list_of_cards.list_of_cards_frame.list.delete(card_to_remove)
    # helpers.screen_cleaner()
    # interface_populating.interface_population(cards)

    with open("my_cards.txt", "w") as file:
        file.writelines("\n".join(card_links))


#


CARDS_PER_FRAME = 3
all_images = []


def add_card():
    new_window = tk.Toplevel(bg="grey42")

    new_window.minsize(width=500, height=300)

    the_card = helpers.searching_card_to_add(new_window)

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
                                    command=lambda i=indexes: helpers.saving_the_card(each_variant_uri[i], new_window))
            card_button.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
            indexes += 1
            sleep(0.5)
