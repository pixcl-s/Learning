from interface import app
import interface_populating
import list_of_cards
from cards_info import card_info


if __name__ == "__main__":
    interface_populating.interface_population(card_info)
    app.root.mainloop()


# https://www.geeksforgeeks.org/what-are-widgets-in-tkinter/

