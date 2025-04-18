
import tkinter as tk
from abc import ABC, abstractmethod

# from cards_info import card_info

# card_info = card_info

# card_info = ["pesho", "gosho", "dobri", "alex", "aha"]


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MTGPrices")
        self.root.geometry("1685x887")
        self.root.resizable(False, False)


        self.root.columnconfigure(0, weight=5)
        # self.root.columnconfigure(1, weight=3)
        self.root.columnconfigure(2, weight=1)
        # self.root.columnconfigure(3, weight=3)
        # self.root.columnconfigure(4, weight=1)
        self.root.rowconfigure(1, weight=3)
        # self.root.rowconfigure(2, weight=3)
        # self.root.rowconfigure(3, weight=3)


class Frames(ABC):
    def __init__(self, main: "Main"):
        self.frame = tk.Frame(main.root, bg="grey15")

    @abstractmethod
    def grid(self, *args):
        pass


class SearchFrame(Frames):
    def __init__(self, main: "Main"):
        super().__init__(main)

        self.label = tk.Label(self.frame, text="Search:", bg="grey22", fg="snow")
        self.entry = tk.Entry(self.frame, bg="grey22", fg="snow")

        self.frame.columnconfigure(1, weight=1)

    def grid(self):
        self.frame.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1, sticky="ew")





# TO DO
# Multiple frames for cards - 4
app = Main()
# app.root.minsize(width=1200, height=900)

search_frame = SearchFrame(app)
search_frame.grid()

# list_of_cards_frame = ListOfCards(app)
# list_of_cards_frame.grid()




# cards_frame_three = CardsFrame(app)
# cards_frame_three.grid(2, 0)
# cards_frame_three.frame.configure(bg="grey25")
#
# cards_frame_four = CardsFrame(app)
# cards_frame_four.grid(2, 1)
# cards_frame_four.frame.configure(bg="grey30")

# cards
# with open("my_cards.txt", "r") as file:
#     cards = [x.strip() for x in file.readlines()]


# class ListOfCards(Frames):
#     def __init__(self, main: "Main"):
#         super().__init__(main)
#
#         self.list = tk.Listbox(self.frame, bg="grey22", fg="snow", activestyle="none", selectforeground="black", font=('Tahoma', 15))
#         self.add_button = tk.Button(self.frame, text="Add", bg="grey26", fg="snow", width=10)  # , command=add_to_list_of_cards)
#         self.remove_button = tk.Button(self.frame, text="Remove", command=commands.remove_from_list_of_cards, bg="grey26", fg="snow", width=10)  # )
#
#         self.frame.columnconfigure(0, weight=1)
#         self.frame.rowconfigure(0, weight=1)
#
#         for index, card in enumerate(card_info):
#             self.list.insert(index, card)
#
#     def grid(self) -> None:
#         self.frame.grid(row=1, column=4, sticky="nsew")
#         self.list.grid(row=0, column=0, sticky="nsew")
#         self.add_button.grid(row=1, column=0, sticky="w")
#         self.remove_button.grid(row=1, column=0, sticky="e")


# url = "https://cards.scryfall.io/border_crop/front/a/5/a577ba08-0aa8-45be-aa83-d5078770127c.jpg?1736468492"
# response = requests.get(url)
# img_data = response.content

# img_resize = Image.open(BytesIO(img_data)).resize((162, 227))
# img = ImageTk.PhotoImage(img_resize)

# the_image = tk.Label(cards_frame_one.frame, image=img, bg="grey22")
# the_image.grid(row=0, column=0, padx=10, pady=10)


# frame_in_frame = tk.Frame(cards_label_one.frame, bg="grey2", width=162, height=227)
# frame_in_frame.grid(row=0, column=0, padx=10, pady=10)
# frame_in_frame.grid_propagate(False)

# card_name = tk.Label(frame_in_frame, bg="grey22", fg="snow", text="Edgar-chan", font=('Tahoma', 15))
# card_name.grid(row=0, column=0, padx=10, pady=10)
# card_kingdom = tk.Label(frame_in_frame, bg="grey22", fg="snow", text="Card Kingdom", font=('Malgun Gothic', 15))
# card_kingdom.grid(row=1, column=0, padx=10, pady=10)
# card_kingdom_price = tk.Label(frame_in_frame, bg="grey22", fg="snow", text="50lea", font=('Calibri', 12))
# card_kingdom_price.grid(row=2, column=0, padx=10, pady=10)


# frame_in_frame2 = tk.Frame(cards_label_two.frame, bg="grey2", width=162, height=227)
# frame_in_frame2.grid(row=0, column=0, padx=10, pady=10)
# frame_in_frame2.grid_propagate(False)


# the_image_2 = tk.Label(cards_frame_two.frame, image=img, bg="grey22")
# the_image_2.grid(row=0, column=0, padx=10, pady=10)
# text_2 = tk.Label(frame_in_frame2, bg="grey22", height=12, width=20, fg="snow", text="Edgar Markov\n\nCardKingdom\n50lea\n\nTCGPlayer\n50lea\n\n\nCommander in\n25555 Decks", font=('Calibri', 12))
# text_2.grid(row=0, column=0, padx=10, pady=10)

# the_image_3 = tk.Label(cards_frame_one.frame, image=img, bg="grey22")
# the_image_3.grid(row=1, column=0, padx=10, pady=10)
# text_3 = tk.Label(cards_label_one.frame, bg="grey22", height=12, width=20, fg="snow", text="Edgar Markov\n\nCardKingdom\n50lea\n\nTCGPlayer\n50lea\n\n\nCommander in\n25555 Decks", font=('Calibri', 12))
# text_3.grid(row=10, column=0, padx=10, pady=10)

# the_image_4 = tk.Label(cards_frame_two.frame, image=img, bg="grey22")
# the_image_4.grid(row=1, column=0, padx=10, pady=10)
# text_4 = tk.Label(cards_label_two.frame, bg="grey22", height=12, width=20, fg="snow", text="Edgar Markov\n\nCardKingdom\n50lea\n\nTCGPlayer\n50lea\n\n\nCommander in\n25555 Decks", font=('Calibri', 12))
# text_4.grid(row=3, column=0, padx=10, pady=10)

# separator = tk.Entry(app.root)
# separator.grid(row=1, column=0, sticky="ew")
# separator = tk.Entry(app.root)
# separator.grid(row=1, column=1, sticky="ew")
# separator = tk.Entry(app.root)
# separator.grid(row=1, column=2, sticky="ew")
# separator = tk.Entry(app.root)
# separator.grid(row=1, column=3, sticky="ew")


#
# # ================================================================================================
# # ================================================================================================
#
# cards_frame = tk.Frame(root)
# cards_frame.grid(row=1, column=0, sticky="nsew")
#
# # cards_list = tk.Listbox(cards_frame, bg="midnight blue")
# # cards_list.grid(sticky="nsew")
#
# cards_frame.columnconfigure(0, weight=1)
# cards_frame.rowconfigure(0, weight=1)
#
# # ================================================================================================
# # ================================================================================================
#
# list_of_cards_frame = tk.Frame(root, bg="grey26")
# list_of_cards_frame.grid(row=1, column=1, sticky="nsew")
#
# list_of_cards_list = tk.Listbox(list_of_cards_frame, bg="grey26", fg="snow")
# list_of_cards_list.grid(row=0, column=0, sticky="nsew")
#
# list_of_cards_button = tk.Button(list_of_cards_frame, text="Add", bg="grey26", fg="snow", command=add_to_list_of_cards)
# list_of_cards_button.grid(row=1, column=0)
#
# list_of_cards_frame.columnconfigure(0, weight=1)
# list_of_cards_frame.rowconfigure(0, weight=1)
##
# # ================================================================================================
# # ================================================================================================
#
#
# def add_to_list_of_cards():
#     text = search_entry.get()
#     if text:
#         list_of_cards_list.insert(tk.END, text)
#         search_entry.delete(0, tk.END)
#
#
# # ================================================================================================
# # ================================================================================================
#

# root.columnconfigure(0, weight=5)
# root.columnconfigure(1, weight=1)
# root.rowconfigure(1, weight=1)
# search_frame = tk.Frame(root, bg="grey15")
# search_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
#
# search_label = tk.Label(search_frame, text="Search:", bg="grey15", fg="snow")
# search_label.grid(row=0, column=0, sticky="w")
#
# search_entry = tk.Entry(search_frame, bg="grey15", fg="snow")
# search_entry.grid(row=0, column=1, sticky="ew")
#
# search_frame.columnconfigure(1, weight=1)







# https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html


# columnspan="2"
# entry.bind("<Return>", lambda event: add_to_list_of_cards) add text when enter is pressed

# def on_click():
#     button.config(text="Added")
#
#
# label = tk.Label(root, text="Search")
# label.grid(row=0, column=0)
#
# # print(label.config().keys())
#
# button = tk.Button(root, text="Add", command=on_click)
# button.grid()
#
# # print(button.config().keys())
