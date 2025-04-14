import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
from time import sleep
import requests
from interface import cards_frame_one, cards_label_one, cards_frame_two, cards_label_two
from cards_info import card_info
from prices import cardkingdom_price, tcgplayer_price, cardmarket_price

card_info = card_info

all_images = []


def interface_population(list_of_cards):
    row = 0

    all_images.clear()
    card_images = [x["image_uris"]["border_crop"] for x in list_of_cards.values()]
    card_names = [x["name"] for x in list_of_cards.values()]
    edh_rec_url = [x["related_uris"]["edhrec"] for x in list_of_cards.values()]
    tcgplayer_url = [x["purchase_uris"]["tcgplayer"] for x in list_of_cards.values()]
    cardmarket_url = [x["purchase_uris"]["cardmarket"] for x in list_of_cards.values()]

    for i in range(len(card_images)):
        #  IMAGES AND LABELS
        current_img_url = card_images[i]
        response_img = requests.get(current_img_url)
        img_data = response_img.content

        img_resize = Image.open(BytesIO(img_data)).resize((162, 227))
        img = ImageTk.PhotoImage(img_resize)
        all_images.append(img)

        current_card_name = card_names[i]

        cardmarket_info = cardmarket_price(cardmarket_url[i])

        if i % 2 == 0:
            # IMAGE
            tk.Label(cards_frame_one.frame, image=img, bg="grey22").grid(row=row, column=0, padx=10, pady=10)

            # LABELS
            frame_in_frame = tk.Frame(cards_label_one.frame, bg="grey2")  # , width=162, height=227
            frame_in_frame.grid(row=row, column=0, padx=10, pady=10)
            # frame_in_frame.grid_propagate(False)
            # frame_in_frame.rowconfigure(0, weight=1)
            # frame_in_frame.rowconfigure(1, weight=1)
            # frame_in_frame.rowconfigure(2, weight=1)

            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=current_card_name, font=("Tahoma", 15)).grid(row=0, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"Card Kingdom: ~{cardkingdom_price(edh_rec_url[i])}$", font=("Malgun Gothic", 15)).grid(row=1, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"TCGplayer: {tcgplayer_price(tcgplayer_url[i])}", font=("Calibri", 12)).grid(row=2, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"Cardmarket", font=("Calibri", 12)).grid(row=3, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"availability: {cardmarket_info['available_items']}", font=("Calibri", 12)).grid(row=4, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"lowest price: {cardmarket_info['lowest_price']}", font=("Calibri", 12)).grid(row=4, column=1)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"price trend: {cardmarket_info['price_trend']}", font=("Calibri", 12)).grid(row=4, column=2)

        else:
            # IMAGE
            tk.Label(cards_frame_two.frame, image=img, bg="grey22").grid(row=row, column=0, padx=10, pady=10)

            # LABELS
            frame_in_frame = tk.Frame(cards_label_two.frame, bg="grey2", width=162, height=227)
            frame_in_frame.grid(row=row, column=0, padx=10, pady=10)

            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=current_card_name, font=("Tahoma", 15)).grid(row=0, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"Card Kingdom: ~{cardkingdom_price(edh_rec_url[i])}$", font=("Malgun Gothic", 15)).grid(row=1, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"TCGplayer: {tcgplayer_price(tcgplayer_url[i])}", font=("Calibri", 12)).grid(row=2, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"Cardmarket", font=("Calibri", 12)).grid(row=3,
                                                                                                            column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"availability: {cardmarket_info['available_items']}",
                     font=("Calibri", 12)).grid(row=4, column=0)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"lowest price: {cardmarket_info['lowest_price']}",
                     font=("Calibri", 12)).grid(row=4, column=1)
            tk.Label(frame_in_frame, bg="grey22", fg="snow", text=f"price trend: {cardmarket_info['price_trend']}",
                     font=("Calibri", 12)).grid(row=4, column=2)

            row += 1
        sleep(0.5)


# def card_img():
#     for card in card_info.values():
#         yield card["image_uris"]["border_crop"]
#
#
# def card_names():
#     for card in card_info.values():
#         yield card["name"]
# img_generator = card_img()
# name_generator = card_names()
