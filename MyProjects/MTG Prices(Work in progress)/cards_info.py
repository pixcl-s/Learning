# import requests
#
# base_url = "https://api.scryfall.com/cards/named?fuzzy="
#
# headers = {"User-Agent": "MTGPrices", "Accept": "*/*"}
#
# card_name_search = "kindred dominance"
#
# response = requests.get(base_url + card_name_search, headers=headers)
# card_data = response.json()
# # response.status_code
# # card_info = response.json()
# # print(response.text)
# # https://scryfall.com/docs/api/cards/named
#
# card_name = card_data["name"]
# png = card_data["image_uris"]["border_crop"]
# edh_rec = card_data["related_uris"]["edhrec"]
# tcg_player = card_data["purchase_uris"]["tcgplayer"]
# card_market = card_data["purchase_uris"]["cardmarket"]
#
# variants_link = card_data["prints_search_uri"]
# variants_response = requests.get(variants_link)
# variants_data = variants_response.json()
#
# variants_amount = variants_data["total_cards"]
# variants = variants_data["data"]
# each_variant = {x["uri"]: x["image_uris"]["border_crop"] for x in variants}
#
# print(card_name)
# print(png)
# print(edh_rec)
# print(tcg_player)
# print(card_market)
# print(variants_link)
# # print()
# print(each_variant)


# def card_neim():
#     return card_name
#
#
# def card_png():
#     return png

# ================================
import requests
from time import sleep

with open("my_cards.txt", "r") as file:
    cards = [x.strip() for x in file.readlines()]


def base_url():
    return "https://api.scryfall.com/cards/named?fuzzy="


def headers():
    return {"User-Agent": "MTGPrices", "Accept": "*/*"}


def the_info(card: list):
    info = {}
    for x in card:
        response = requests.get(x, headers=headers())
        data = response.json()
        info[data["name"]] = data
        sleep(0.5)

    return info


card_info = the_info(cards)


def get_card(card_name):
    card_name = card_name

    response = requests.get(base_url() + card_name, headers=headers())
    card_data = response.json()

    sleep(0.5)

    return card_data


def each_card_variant(card_name):
    the_card = get_card(card_name)
    variants_link = the_card["prints_search_uri"]
    variants_response = requests.get(variants_link)
    variants_data = variants_response.json()

    each_variant = {x["image_uris"]["border_crop"]: x["uri"] for x in variants_data["data"]}
    variants_amount = variants_data["total_cards"]

    sleep(0.5)

    return each_variant, variants_amount
