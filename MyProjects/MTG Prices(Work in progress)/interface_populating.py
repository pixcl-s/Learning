import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
from time import sleep
import requests
import helpers
from cards_frame import card_frame_one, card_label_one, card_frame_two, card_label_two
from cards_info import card_info
from prices import cardkingdom_price, tcgplayer_price, cardmarket_price

card_info = card_info

saving_images = []


def interface_population(list_of_cards):
    card_images = [x["image_uris"]["border_crop"] for x in list_of_cards.values()]
    card_names = [x["name"] for x in list_of_cards.values()]
    card_colors = [x["colors"][0] if len(x["colors"]) == 1 else "Y" for x in list_of_cards.values()]

    edh_rec_url = [x["related_uris"]["edhrec"] for x in list_of_cards.values()]
    tcgplayer_url = [x["purchase_uris"]["tcgplayer"] for x in list_of_cards.values()]
    cardmarket_url = [x["purchase_uris"]["cardmarket"] for x in list_of_cards.values()]
    scryfall_url = [x["scryfall_uri"] for x in list_of_cards.values()]

    for i in range(len(card_images)):
        #  IMAGES AND LABELS
        current_img_url = card_images[i]
        response_img = requests.get(current_img_url)
        img_data = response_img.content
        img_resize = Image.open(BytesIO(img_data)).resize((162, 230))
        img = ImageTk.PhotoImage(img_resize)
        saving_images.append(img)

        current_card_name = card_names[i]
        current_card_color = card_colors[i]
        background_color, foreground_color = helpers.colors(current_card_color)

        current_scryfall_url = scryfall_url[i]
        current_edh_rec_url = edh_rec_url[i]
        current_tcgplayer_url = tcgplayer_url[i]
        current_cardmarket_url = cardmarket_url[i]

        cardmarket_prices = cardmarket_price(current_cardmarket_url)
        tcgplayer_prices = tcgplayer_price(current_tcgplayer_url)
        cardkingdom_prices = f"~{cardkingdom_price(current_edh_rec_url)}$"

        def the_populating(frames, labels):
            tk.Label(frames, bg="grey12", height=1).pack(fill=tk.X)
            tk.Label(labels, bg="grey12", height=1).pack(fill=tk.X)
            # IMAGE
            tk.Label(frames, image=img, bg="grey12", width=166, height=234).pack(pady=9)

            # LABELS
            frame_in_frame = tk.Frame(labels, bg="grey12")
            frame_in_frame.pack(fill=tk.BOTH, padx=10, pady=11)


#       ================================================== card  name ==================================================

            name = tk.Label(frame_in_frame,
                            bg=background_color,
                            fg=foreground_color,
                            text=current_card_name,
                            font=("Tahoma", 15), cursor="hand2", relief=tk.SUNKEN)

            name.pack(expand=True, fill=tk.X)
            name.bind("<Button-1>", lambda x, y=current_scryfall_url: helpers.browser(y))


#       =============================================== card market info ===============================================

            cardmarket = tk.Label(frame_in_frame,
                                  bg=background_color,
                                  fg=foreground_color,
                                  text=f"= Cardmarket =",
                                  font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)

            cardmarket.pack(expand=True, fill=tk.X)
            cardmarket.bind("<Button-1>", lambda x, y=current_cardmarket_url: helpers.browser(y))

            tk.Label(frame_in_frame,
                     bg=background_color,
                     fg=foreground_color,
                     text=f"Available: {cardmarket_prices['available_items']}\n"
                          f"Lowest Price: {cardmarket_prices['lowest_price']}\n"
                          f"Price Trend: {cardmarket_prices['price_trend']}",
                     font=("Calibri", 12), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)


#       ================================================ tcgplayer info ================================================

            tcgplayer = tk.Label(frame_in_frame,
                                 bg=background_color,
                                 fg=foreground_color,
                                 text=f"= TCG Player =",
                                 font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)

            tcgplayer.pack(expand=True, fill=tk.X)
            tcgplayer.bind("<Button-1>", lambda x, y=current_tcgplayer_url: helpers.browser(y))

            tk.Label(frame_in_frame,
                     bg=background_color,
                     fg=foreground_color,
                     text=tcgplayer_prices,
                     font=("Calibri", 13), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)


#       =============================================== cardkingdom info ===============================================

            cardkingdom_edh = tk.Label(frame_in_frame,
                                       bg=background_color,
                                       fg=foreground_color,
                                       text=f"= Card Kingdom =",
                                       font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)

            cardkingdom_edh.pack(expand=True, fill=tk.X)
            cardkingdom_edh.bind("<Button-1>", lambda x, y=current_edh_rec_url: helpers.browser(y))

            tk.Label(frame_in_frame,
                     bg=background_color,
                     fg=foreground_color,
                     text=cardkingdom_prices,
                     font=("Calibri", 13), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)

        if (len(saving_images)-1) % 2:
            the_populating(card_frame_two.frame, card_label_two.frame)
        else:
            the_populating(card_frame_one.frame, card_label_one.frame)

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


# tk.Label(card_frame_one.frame, bg="grey1", height=1).pack(fill=tk.X)
# tk.Label(card_label_one.frame, bg="grey1", height=1).pack(fill=tk.X)
# # IMAGE
# tk.Label(card_frame_one.frame, image=img, bg="grey1").pack(padx=10, pady=10)
#
# # LABELS
# frame_in_frame = tk.Frame(card_label_one.frame, bg="grey1")  # , width=162, height=227
# frame_in_frame.pack(fill=tk.BOTH, padx=10, pady=10)
#
# name = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color,
#                 text=current_card_name,
#                 font=("Tahoma", 15), cursor="hand2", relief=tk.SUNKEN)
# name.pack(expand=True, fill=tk.X)
# name.bind("<Button-1>", lambda x, y=current_scryfall_url: helpers.browser(y))
#
# cardmarket = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=f"= Cardmarket =", font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)
# cardmarket.pack(expand=True, fill=tk.X)
# cardmarket.bind("<Button-1>", lambda x, y=current_cardmarket_url: helpers.browser(y))
#
# tk.Label(frame_in_frame, bg=background_color, fg=foreground_color,
#          text=f"Available: {cardmarket_prices['available_items']}\n"
#               f"Lowest Price: {cardmarket_prices['lowest_price']}\n"
#               f"Price Trend: {cardmarket_prices['price_trend']}",
#          font=("Calibri", 12), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)
#
# tcgplayer = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=f"= TCG Player =", font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)
# tcgplayer.pack(expand=True, fill=tk.X)
# tcgplayer.bind("<Button-1>", lambda x, y=current_tcgplayer_url: helpers.browser(y))
# tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=tcgplayer_prices, font=("Calibri", 13), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)
#
# cardkingdom_edh = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=f"= Card Kingdom =", font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)
# cardkingdom_edh.pack(expand=True, fill=tk.X)
# cardkingdom_edh.bind("<Button-1>", lambda x, y=current_edh_rec_url: helpers.browser(y))
#
# tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=cardkingdom_prices,
#          font=("Calibri", 13), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)


# tk.Label(card_frame_two.frame, bg="grey1", height=1).pack(fill=tk.X)
# tk.Label(card_label_two.frame, bg="grey1", height=1).pack(fill=tk.X)
# # IMAGE
# tk.Label(card_frame_two.frame, image=img, bg="grey1").pack(padx=10, pady=10)
#
# # LABELS
# frame_in_frame = tk.Frame(card_label_two.frame, bg="grey1")  # , width=162, height=227
# frame_in_frame.pack(fill=tk.BOTH, padx=10, pady=10)
#
# name = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color,
#                 text=current_card_name,
#                 font=("Tahoma", 15), cursor="hand2", relief=tk.SUNKEN)
# name.pack(expand=True, fill=tk.X)
# name.bind("<Button-1>", lambda x, y=current_scryfall_url: helpers.browser(y))
#
# cardmarket = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=f"= Cardmarket =",
#                       font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)
# cardmarket.pack(expand=True, fill=tk.X)
# cardmarket.bind("<Button-1>", lambda x, y=current_cardmarket_url: helpers.browser(y))
#
# tk.Label(frame_in_frame, bg=background_color, fg=foreground_color,
#          text=f"Available: {cardmarket_prices['available_items']}\n"
#               f"Lowest Price: {cardmarket_prices['lowest_price']}\n"
#               f"Price Trend: {cardmarket_prices['price_trend']}",
#          font=("Calibri", 12), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)
#
# tcgplayer = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=f"= TCG Player =",
#                      font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)
# tcgplayer.pack(expand=True, fill=tk.X)
# tcgplayer.bind("<Button-1>", lambda x, y=current_tcgplayer_url: helpers.browser(y))
# tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=tcgplayer_prices, font=("Calibri", 13),
#          relief=tk.SUNKEN).pack(expand=True, fill=tk.X)
#
# cardkingdom_edh = tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=f"= Card Kingdom =",
#                            font=("Calibri", 14), cursor="hand2", relief=tk.SUNKEN)
# cardkingdom_edh.pack(expand=True, fill=tk.X)
# cardkingdom_edh.bind("<Button-1>", lambda x, y=current_edh_rec_url: helpers.browser(y))
#
# tk.Label(frame_in_frame, bg=background_color, fg=foreground_color, text=cardkingdom_prices,
#          font=("Calibri", 13), relief=tk.SUNKEN).pack(expand=True, fill=tk.X)
