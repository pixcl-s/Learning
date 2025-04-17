import tkinter as tk
import interface
import commands
from cards_info import card_info

cards = card_info


class ListOfCards(interface.Frames):
    def __init__(self, main):
        super().__init__(main)

        self.list = tk.Listbox(self.frame, bg="grey22", fg="snow", activestyle="none", selectforeground="black", font=('Tahoma', 15))
        self.add_button = tk.Button(self.frame, text="Add", command=commands.add_card, bg="grey26", fg="snow", width=10)
        self.remove_button = tk.Button(self.frame, text="Remove", command=commands.remove_cards, bg="grey26", fg="snow", width=10)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        for index, card in enumerate(cards):
            self.list.insert(index, card)

    def grid(self) -> None:
        self.frame.grid(row=1, column=2, sticky="nsew")
        self.list.grid(row=0, column=0, sticky="nsew")
        self.add_button.grid(row=1, column=0, sticky="w")
        self.remove_button.grid(row=1, column=0, sticky="e")


list_of_cards_frame = ListOfCards(interface.app)
list_of_cards_frame.grid()
