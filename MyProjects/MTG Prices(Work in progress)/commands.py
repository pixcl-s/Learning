import tkinter as tk
from time import sleep
import requests
from io import BytesIO
import interface_populating
from cards_info import card_info, each_card_variant, get_card, the_info
import list_of_cards
import helpers
from math import ceil
from PIL import Image, ImageTk
import cards_frame


cards = card_info


# def remove_cards():
#     card_to_remove_index = list_of_cards.list_of_cards_frame.list.curselection()[0]
#     card_name = list_of_cards.list_of_cards_frame.list.get(0, tk.END)[card_to_remove_index]
#     # listbox.get(listbox.curselection())
#
#     del cards[card_name]
#
#     card_links = [x['uri'] for x in cards.values()]
#
#     list_of_cards.list_of_cards_frame.list.delete(card_to_remove_index)
#     helpers.screen_cleaner()
#     interface_populating.interface_population(cards)
#
#     with open("my_cards.txt", "w") as file:
#         file.writelines("\n".join(card_links))

def remove_cards():
    card_to_remove_index = list_of_cards.list_of_cards_frame.list.curselection()[0]
    card_name = list_of_cards.list_of_cards_frame.list.get(0, tk.END)[card_to_remove_index]
    # listbox.get(listbox.curselection())

    all_widgets = []

    images_one = cards_frame.card_frame_one.frame.winfo_children()
    prices_one = cards_frame.card_label_one.frame.winfo_children()

    images_two = cards_frame.card_frame_two.frame.winfo_children()
    prices_two = cards_frame.card_label_two.frame.winfo_children()

    for x in range(len(images_one) // 2):
        combination_one = []
        combination_two = []

        combination_one.extend(images_one[1:2])
        combination_one.extend(prices_one[1:2])
        del images_one[:2], prices_one[:2]
        if len(images_two) != 0:
            combination_two.extend(images_two[1:2])
            combination_two.extend(prices_two[1:2])
            del images_two[:2], prices_two[:2]

        all_widgets.append(combination_one)
        if combination_two:
            all_widgets.append(combination_two)

    widgets_replacing = all_widgets[card_to_remove_index:]
    links = interface_populating.saving_links[card_to_remove_index+1:]
    interface_populating.saving_links.pop(card_to_remove_index)

    for index in range(len(widgets_replacing)):
        if index == len(widgets_replacing)-1:
            for widget in all_widgets[-1]:
                widget.destroy()
            break

        img, prices = widgets_replacing[index]
        replacer_img, replacer_prices = widgets_replacing[index+1]

        price_labels = prices.winfo_children()
        replacer_price_labels = replacer_prices.winfo_children()
        link = links[index]

        img.configure(image=replacer_img.cget("image"))

        for i in range(len(price_labels)):
            price_labels[i].configure(bg=replacer_price_labels[i].cget("bg"),
                                      fg=replacer_price_labels[i].cget("fg"),
                                      text=replacer_price_labels[i].cget("text"),
                                      font=replacer_price_labels[i].cget("font"),
                                      cursor=replacer_price_labels[i].cget("cursor"))
            if i in link:
                price_labels[i].bind("<Button-1>", lambda _, l=link[i]: helpers.browser(l))

    del cards[card_name]

    card_links = [x['uri'] for x in cards.values()]

    list_of_cards.list_of_cards_frame.list.delete(card_to_remove_index)
    # helpers.screen_cleaner()
    # interface_populating.interface_population(cards)

    with open("my_cards.txt", "w") as file:
        file.writelines("\n".join(card_links))

#
# def searching_card_to_add(window):
#     searched_card_name = tk.StringVar(window)
#
#     card_entry_label = tk.Label(window, text="Card Name", bg="grey22", fg="snow")
#     card_entry_label.pack(side=tk.LEFT)
#
#     card_entry = tk.Entry(window, bd=3, bg="grey22", fg="snow", width="50")  # , textvariable=searched_card_name
#     card_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
#
#     card_entry_button = tk.Button(window, text="Confirm", bg="grey22", fg="snow",
#                                   command=lambda: searched_card_name.set(card_entry.get()))
#     card_entry_button.pack(side=tk.LEFT)
#
#     card_entry.bind("<Return>", lambda btn: card_entry_button)
#
#     card_entry_button.wait_variable(searched_card_name)
#
#     card_entry_label.destroy()
#     card_entry.destroy()
#     card_entry_button.destroy()
#
#     return searched_card_name.get()


# def add_card():
#     new_window = tk.Toplevel(bg="grey42")
#
#     new_window.minsize(width=500, height=300)
#
#     the_card = searching_card_to_add(new_window)
#
#     frames = []
#     each_variant, amount = each_card_variant(the_card)
#     each_variant_png = list(each_variant.keys())
#     each_variant_uri = list(each_variant.values())
#
#     for _ in range(ceil(amount / CARDS_PER_FRAME)):
#         frame = tk.Frame(new_window, bg="grey22")
#         frame.pack(fill=tk.BOTH, expand=True)
#         frames.append(frame)
#
#     indexes = 0
#
#     for x in frames:
#         for _ in range(CARDS_PER_FRAME):
#             if indexes == len(each_variant_png):
#                 break
#
#             current_img = each_variant_png[indexes]
#             response_img = requests.get(current_img)
#             img_data = response_img.content
#
#             img_resize = Image.open(BytesIO(img_data)).resize((162, 227))
#             img = ImageTk.PhotoImage(img_resize)
#             all_images.append(img)
#
#             card_button = tk.Button(x, image=img, bd=5, bg="grey22",
#                                     command=lambda i=indexes: helpers.saving_the_card(each_variant_uri[i], new_window))
#             card_button.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
#             indexes += 1
#             sleep(0.5)

class CardAdd:
    CARDS_PER_FRAME = 5

    def __init__(self):
        self.new_window = tk.Toplevel(bg="grey22")
        self.searching_frame = tk.Frame(self.new_window, bg="grey22")
        self.card_entry_label = tk.Label(self.searching_frame, text="Card Name", bg="grey22", fg="snow",
                                         font=("Calibri", 13))
        self.card_entry = tk.Entry(self.searching_frame, bd=3, bg="grey22", fg="snow", width=50, font=("Calibri", 12))
        self.card_entry_button = tk.Button(self.searching_frame,
                                           text="Confirm", bg="grey22", fg="snow",
                                           command=lambda: self.getting_card(self.card_entry.get()),
                                           font=("Calibri", 11))

        self.new_window.minsize(width=1040, height=675)
        self.searching_frame.pack()
        self.card_entry_label.pack(side="left")
        self.card_entry.pack(side="left", )
        self.card_entry.focus_set()
        self.card_entry_button.pack(side="left")
        self.card_entry.bind("<Return>", lambda _: self.getting_card(self.card_entry.get()))

        self.all_images = []

    def getting_card(self, text):
        self.card_entry.delete(0, tk.END)

        if self.new_window.winfo_children() != 1:
            [x.destroy() for x in self.new_window.winfo_children()[1:]]

        if text:
            the_card = get_card(text)
            if the_card:
                self.stuff(the_card)
                return

        tk.Label(self.new_window, text="card not found", bg="grey22", fg="snow", font=("Calibri", 16)).pack()

    def stuff(self, card):
        each_variant, amount = each_card_variant(card)
        each_variant_png = list(each_variant.keys())
        each_variant_info = list(each_variant.values())
        each_variant_uri = [x["uri"] for x in each_variant.values()]

        frames = []

        try:
            self.new_window.winfo_children()[1].configure(text=f"Variants: {amount}")
        except Exception:
            tk.Label(self.new_window, text=f"Variants: {amount}", bg="grey22", fg="snow", font=("Calibri", 16)).pack()

        for _ in range(ceil(amount / self.CARDS_PER_FRAME)):
            frame = tk.Frame(self.new_window, bg="grey22")
            frame.pack()
            frames.append(frame)

        indexes = 0

        for x in frames:
            for _ in range(self.CARDS_PER_FRAME):
                if indexes == len(each_variant_png):
                    break

                current_img = each_variant_png[indexes]
                current_variant_info = each_variant_info[indexes]

                response_img = requests.get(current_img)
                sleep(0.5)
                img_data = response_img.content
                img_resize = Image.open(BytesIO(img_data)).resize((182, 247))
                img = ImageTk.PhotoImage(img_resize)
                self.all_images.append(img)

                card_button = tk.Button(x, image=img,
                                        text=f"set: {current_variant_info['set'].upper()}  "
                                             f"  # {current_variant_info['collector_number']}",
                                        bd=3, bg="grey12", fg="snow", compound="top", font=("Calibri", 10),
                                        command=lambda i=indexes: self.saving_the_card(each_variant_info[i],
                                                                                       each_variant_uri[i]))
                card_button.pack(side=tk.LEFT, padx=8, pady=8)
                indexes += 1

    def saving_the_card(self, info, uri):
        self.new_window.destroy()
        with open("my_cards.txt", "a") as file:
            file.write("\n" + uri)
        the_card = {info["name"]: info}
        cards.update(the_card)

        interface_populating.interface_population(the_card)
        list_of_cards.list_of_cards_frame.list.insert(tk.END, list(the_card.keys())[0])
