from webbrowser import open_new_tab
import tkinter as tk
import cards_frame
import list_of_cards
from cards_info import card_info, the_info
import interface_populating
import commands

cards = card_info

the_frames = [cards_frame.card_frame_one,
              cards_frame.card_frame_two,
              cards_frame.card_label_one,
              cards_frame.card_label_two]

all_colors = {"W": ["antiquewhite1", "grey1"],
              "U": ["royalblue", "snow"],
              "B": ["grey17", "snow"],
              "R": ["firebrick3", "snow"],
              "G": ["palegreen4", "grey1"],
              "Y": ["lightgoldenrod1", "grey1"]}


def screen_cleaner():
    for x in the_frames:
        for y in x.frame.pack_slaves():
            y.destroy()


def searching_card_to_add(window):
    searched_card_name = tk.StringVar(window)

    card_entry_label = tk.Label(window, text="Card Name", bg="grey22", fg="snow")
    card_entry_label.pack(side=tk.LEFT)

    card_entry = tk.Entry(window, bd=3, bg="grey22", fg="snow", width="50")  # , textvariable=searched_card_name
    card_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    card_entry_button = tk.Button(window, text="Confirm", bg="grey22", fg="snow",
                                  command=lambda: searched_card_name.set(card_entry.get()))
    card_entry_button.pack(side=tk.LEFT)

    card_entry.bind("<Return>", lambda btn: card_entry_button)

    card_entry_button.wait_variable(searched_card_name)

    card_entry_label.destroy()
    card_entry.destroy()
    card_entry_button.destroy()

    return searched_card_name.get()


def saving_the_card(uri, window):
    window.destroy()
    commands.all_images.clear()
    with open("my_cards.txt", "a") as file:
        file.write("\n" + uri)
    the_card = the_info([uri])
    cards.update(the_card)

    interface_populating.interface_population(the_card)
    list_of_cards.list_of_cards_frame.list.insert(tk.END, list(the_card.keys())[0])


def browser(url):
    open_new_tab(url)


def colors(color):
    return all_colors[color]
