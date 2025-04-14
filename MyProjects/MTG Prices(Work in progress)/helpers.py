from webbrowser import open_new_tab
from time import sleep
import tkinter as tk
import requests
import interface
import list_of_cards
from cards_info import card_info, the_info
import interface_populating

card_info = card_info
the_frames = [interface.cards_frame_one, interface.cards_frame_two, interface.cards_label_one, interface.cards_label_two]
all_colors = {"W": ["antiquewhite1", "grey1"],
              "U": ["royalblue", "snow"],
              "B": ["grey17", "snow"],
              "R": ["firebrick3", "snow"],
              "G": ["palegreen4", "grey1"],
              "Y": ["lightgoldenrod1", "grey1"]}


def screen_cleaner():
    for x in the_frames:
        for y in x.frame.grid_slaves():
            y.destroy()
            print(y)
        print(x)


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


def saving_the_card(uri):
    with open("my_cards.txt", "a") as file:
        file.write(uri + "\n")
    the_card = the_info([uri])
    card_info.update(the_card)

    screen_cleaner()

    interface_populating.interface_population(card_info)
    list_of_cards.list_of_cards_frame.list.insert(tk.END, list(the_card.keys())[0])


def browser(url):
    open_new_tab(url)


def colors(color):
    return all_colors[color]