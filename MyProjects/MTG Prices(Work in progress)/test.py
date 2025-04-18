# # import cloudscraper
# #
# # cookies = {
# #     '_fbp': 'fb.1.1726329987305.686354820688884247',
# #     '_uetvid': '4c21b40072b311ef934a4f02a22642b3',
# #     'PHPSESSID': 'juuvndu58cpqb76n4b8cshg8jj',
# #     '_cfuvid': '6M3cBzmxv_jn5NNCP_mkRf1tcDZxzySRICGHr.gUGwQ-1744375357316-0.0.1.1-604800000',
# #     '__cf_bm': 'fDLLv6D4PsDOYuF5QXzCgcvfSwNTNg2hgEPBKvOOrJ8-1744383413-1.0.1.1-8Lnnmk.sMvRX9WwRL76ZvWoexUQxnYhUDfbm9DOMzOcoCxk.v4F2HbNNFpInSZKUmrHj7hwiF.kIcRJhuFnXuU8nDJfGTcfIOvKnowZLrOM',
# # }
# #
# # headers = {
# #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# #     'accept-language': 'en-US,en;q=0.9',
# #     'cache-control': 'max-age=0',
# #     'priority': 'u=0, i',
# #     'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
# #     'sec-ch-ua-mobile': '?0',
# #     'sec-ch-ua-platform': '"Windows"',
# #     'sec-fetch-dest': 'document',
# #     'sec-fetch-mode': 'navigate',
# #     'sec-fetch-site': 'none',
# #     'sec-fetch-user': '?1',
# #     'upgrade-insecure-requests': '1',
# #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
# #     # 'cookie': '_fbp=fb.1.1726329987305.686354820688884247; _uetvid=4c21b40072b311ef934a4f02a22642b3; PHPSESSID=juuvndu58cpqb76n4b8cshg8jj; _cfuvid=6M3cBzmxv_jn5NNCP_mkRf1tcDZxzySRICGHr.gUGwQ-1744375357316-0.0.1.1-604800000; __cf_bm=fDLLv6D4PsDOYuF5QXzCgcvfSwNTNg2hgEPBKvOOrJ8-1744383413-1.0.1.1-8Lnnmk.sMvRX9WwRL76ZvWoexUQxnYhUDfbm9DOMzOcoCxk.v4F2HbNNFpInSZKUmrHj7hwiF.kIcRJhuFnXuU8nDJfGTcfIOvKnowZLrOM',
# # }
# #
# # params = {
# #     'utm_campaign': 'card_prices',
# #     'utm_medium': 'text',
# #     'utm_source': 'scryfall',
# # }
# #
# # scraper = cloudscraper.create_scraper()
# #
# # response = scraper.get(
# #     'https://www.cardmarket.com/en/Magic/Products/Singles/Innistrad-Remastered/Edgar-Markov',
# #     params=params,
# #     cookies=cookies,
# #     headers=headers,
# # )
# #
# # print(response.status_code)
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from bs4 import BeautifulSoup
#
# options = uc.ChromeOptions()
# # options.headless = True
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
#
# driver = uc.Chrome(options=options)
# driver.get("https://www.cardmarket.com/en/Magic/Products/Singles/Innistrad-Remastered/Edgar-Markov?referrer=scryfall")
#
#
# sleep(10)
#
# try:
#     accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
#     accept_button.click()  # Click the accept button to allow cookies
#     sleep(2)  # Wait for a moment to ensure cookies are accepted
# except:
#     print("No cookie consent modal found or already accepted.")
#
# prices = driver.find_elements(By.TAG_NAME, "dd")[4:7]
# # prices = driver.page_source
# # soup = BeautifulSoup(prices, "lxml")
# for x in prices:
#     print(x.text)
#
# driver.quit()

# from prices import cardmarket_price
#
# print(cardmarket_price("https://www.cardmarket.com/en/Magic/Products/Singles/Innistrad-Remastered/Edgar-Markov?referrer=scryfall&utm_campaign=card_prices&utm_medium=text&utm_source=scryfall"))

# import tkinter as tk
#
# quick = tk.Tk()
# tk.Label(quick, text="lolololol", relief=tk.FLAT, bg="slategray", fg="snow").pack()
# tk.Label(quick, text="lolololol", relief=tk.RAISED, bg="slategray", fg="snow").pack()
# tk.Label(quick, text="lolololol", relief=tk.SUNKEN, bg="slategray", fg="snow").pack()
# tk.Label(quick, text="lolololol", relief=tk.GROOVE, bg="lightslategray", fg="snow").pack()
# tk.Label(quick, text="lolololol", relief=tk.GROOVE, bg="lightslategray", fg="grey1").pack()
# tk.Label(quick, text="lolololol", relief=tk.RIDGE, bg="lightslategray", fg="grey1").pack()
# tk.Label(quick, text="lolololol", bg="snow3", fg="snow", bd=1).pack()
# tk.Label(quick, text="lolololol", bg="snow4", fg="grey1", bd=5).pack()
# tk.Label(quick, bg="red").pack(side=tk.LEFT, fill=tk.Y)
# quick.mainloop()

# from tkinter import *
#
#
# def data():
#     for i in range(50):
#         Label(frame, text=i).grid(row=i, column=0)
#         Label(frame, text="my text"+str(i)).grid(row=i, column=1)
#         Label(frame, text="..........").grid(row=i, column=2)
#
#
# def myfunction(event):
#     canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)
#
#
# from tkinter import *
#
# def data():
#     for i in range(50):
#        Label(frame,text=i).grid(row=i,column=0)
#        Label(frame,text="my text"+str(i)).grid(row=i,column=1)
#        Label(frame,text="..........").grid(row=i,column=2)
#
# def myfunction(event):
#     canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)
#
# root=Tk()
# sizex = 800
# sizey = 600
# posx  = 100
# posy  = 100
# root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
#
# myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
# myframe.place(x=10,y=10)
#
# canvas=Canvas(myframe)
# frame=Frame(canvas)
# myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
# canvas.configure(yscrollcommand=myscrollbar.set)
#
# myscrollbar.pack(side="right",fill="y")
# canvas.pack(side="left")
# canvas.create_window((0,0),window=frame,anchor='nw')
# frame.bind("<Configure>",myfunction)
# data()
# root.mainloop()
# def on_frame_configure(event):
#     main_canvas.configure(scrollregion=main_canvas.bbox("all"))
#
# def resize_frame(event):
#     canvas_width = event.width
#     main_canvas.itemconfig(canvas_window, width=canvas_width)
#
# import tkinter as tk
#
# root = tk.Tk()
#
# main_canvas = tk.Canvas(root, borderwidth=0, bg="grey22")
# v_scrollbar = tk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
# main_canvas.configure(yscrollcommand=v_scrollbar.set)
#
# scrollable_frame = tk.Frame(main_canvas)
#
# canvas_window = main_canvas.create_window((0, 0), window=scrollable_frame)
# scrollable_frame.bind("<Configure>", on_frame_configure)
# main_canvas.bind("<Configure>", resize_frame)
# # Configure scroll region
# v_scrollbar.pack(side="right", fill="y")
# main_canvas.pack(side="left", fill="both", expand=True)
#
# frame_one = tk.Frame(scrollable_frame, bg="yellow")
# frame_two = tk.Frame(scrollable_frame, bg="green")
# frame_three = tk.Frame(scrollable_frame, bg="blue")
# frame_four = tk.Frame(scrollable_frame, bg="red")
# frame_one.pack(side="left", fill="both", expand=True)
# frame_two.pack(side="left", fill=tk.BOTH, expand=True)
# frame_three.pack(side="left", fill=tk.BOTH, expand=True)
# frame_four.pack(side="left", fill=tk.BOTH, expand=True)
#
# # for x in range(50):
# #     tk.Button(frame_one, text=f"looooool {x}").pack()
# #     tk.Button(frame_two, text=f"looooool {x}").pack()
# #     tk.Button(frame_three, text=f"looooool {x}").pack()
# #     tk.Button(frame_four, text=f"looooool {x}").pack()
#
# #
# root.mainloop()

# Optional: Make mouse wheel work
# def on_mousewheel(event):
#     main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
#
# main_canvas.bind_all("<MouseWheel>", on_mousewheel)

# Add your info frames here




# for i in range(4):
#     frame = tk.Frame(scrollable_frame, height=100, width=300, bg=f"#DDDDDD")
#     frame.pack(pady=10, padx=10)
#     tk.Label(frame, text=f"Frame {i+1}").pack()


# import tkinter as tk
#
#
# def funct(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))
#
#
#
# root = tk.Tk()
#
# # root.geometry("800x800-400-100")
#
# frame = tk.Frame(root, bg="blue")
# frame.pack(fill="both", expand=True)
#
# canvas = tk.Canvas(frame, bg="grey5")
# frames = tk.Frame(canvas, bg="yellow")
# scroll = tk.Scrollbar(frame, command=canvas.yview)
#
# canvas.configure(yscrollcommand=scroll.set)
#
#
# scroll.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((0, 0), window=frames)
# # canvas_two.pack(side="left", fill="both", expand=True)
# # canvas_three.pack(side="left", fill="both", expand=True)
# # canvas_four.pack(side="left", fill="both", expand=True)
#
# frames.bind("<Configure>", funct)
#
#
# for x in range(40):
#     tk.Button(frames, text=f"LOOOOL {x}").pack(side="left")
#
#
# root.mainloop()
# import tkinter as tk
#
#
# def printing(num):
#     print(num)
#
#
# root = tk.Tk()
#
# for y in range(4):
#     label = tk.Label(root, text="looooooooool", bg="grey22", fg="snow")
#     label.pack()
#     label.bind("<Button-1>", lambda x, o=y: printing(o))
#
#
# stuff = root.winfo_children()
# for x in stuff:
#     x.bind
# print(stuff)
# # print2.bind.configure(event=print1.cget("event"))
# # widgets = root.winfo_children()
# # label2.configure(text=label.cget("text"), bg=label.cget("bg"))
# # label2.bind("<Button-1>", x)
#
# # print("the label is", label.cget("bg"))
# # print(label.keys())
# # print(label.cget("image"))
# # print(label.winfo_name())
# # print(label2.winfo_name())
# root.mainloop()
import tkinter as tk
import requests
from math import ceil
from time import sleep
from io import BytesIO
from PIL import Image, ImageTk

import cards_info
from cards_info import each_card_variant

# CARDS_PER_FRAME = 5
# all_images = []

# def searching_card_to_add(window):
#     searched_card_name = tk.StringVar(window)
#
#     searching_frame = tk.Frame(window, bg="grey22")
#     searching_frame.pack(fill="x")
#
#     card_entry_label = tk.Label(searching_frame, text="Card Name", bg="grey22", fg="snow", font=("Calibri", 13))
#     card_entry_label.pack(side="left")
#
#     card_entry = tk.Entry(searching_frame, bd=3, bg="grey22", fg="snow", font=("Calibri", 12))  # , textvariable=searched_card_name
#     card_entry.pack(side="left", expand=True, fill="x")
#     card_entry.focus_set()
#
#     # card_entry_button = tk.Button(searching_frame, text="Confirm", bg="grey22", fg="snow",
#     #                               command=lambda: searched_card_name.set(card_entry.get()), font=("Calibri", 11))
#     # card_entry_button.pack(side="left")
#     card_entry_button = tk.Button(searching_frame, text="Confirm", bg="grey22", fg="snow",
#                                   command=lambda x=card_entry.get(): getting_card(x), font=("Calibri", 11))
#     card_entry_button.pack(side="left")
#
#     card_entry.bind("<Return>", lambda btn: searched_card_name.set(card_entry.get()))
#
#     # card_entry_button.wait_variable(searched_card_name)
#
#     # while not searched_card_name.get():
#     #     remove_label = tk.Label(window, text="bruh, enter card name", bg="grey22", fg="snow", font=("Calibri", 15))
#     #     remove_label.pack(side="top")
#     #     card_entry_button.wait_variable(searched_card_name)
#     #     remove_label.destroy()
#
#     # return searched_card_name.get()
#
#
# # def saving_the_card(uri, window):
# #     window.destroy()
# #     commands.all_images.clear()
# #     with open("my_cards.txt", "a") as file:
# #         file.write("\n" + uri)
# #     the_card = the_info([uri])
# #     cards.update(the_card)
# #
# #     interface_populating.interface_population(the_card)
# #     list_of_cards.list_of_cards_frame.list.insert(tk.END, list(the_card.keys())[0])
#
#
# def add_card():
#     new_window = tk.Toplevel(bg="grey22")
#     new_window.minsize(width=500, height=300)
#
#     def stuff(card):
#         each_variant, amount = each_card_variant(card)
#         each_variant_png = list(each_variant.keys())
#         each_variant_info = list(each_variant.values())
#
#         frames = []
#
#         try:
#             new_window.winfo_children()[1].configure(text=f"Variants: {amount}")
#         except Exception:
#             tk.Label(new_window, text=f"Variants: {amount}", bg="grey22", fg="snow", font=("Calibri", 16)).pack()
#
#         for _ in range(ceil(amount / CARDS_PER_FRAME)):
#             frame = tk.Frame(new_window, bg="grey22")
#             frame.pack(fill=tk.BOTH, expand=True)
#             frames.append(frame)
#
#         indexes = 0
#
#         for x in frames:
#             for _ in range(CARDS_PER_FRAME):
#                 if indexes == len(each_variant_png):
#                     break
#
#                 current_img = each_variant_png[indexes]
#                 current_variant_info = each_variant_info[indexes]
#
#                 response_img = requests.get(current_img)
#                 img_data = response_img.content
#                 img_resize = Image.open(BytesIO(img_data)).resize((182, 247))
#                 img = ImageTk.PhotoImage(img_resize)
#                 all_images.append(img)
#
#                 card_button = tk.Button(x, image=img,
#                                         text=f"set: {current_variant_info['set']}  "
#                                              f"  # {current_variant_info['collector_number']}",
#                                         bd=3, bg="grey12", fg="snow", compound="top", font=("Calibri", 10))
#                 # command=lambda i=indexes: saving_the_card(each_variant_uri[i], new_window)
#                 card_button.pack(side=tk.LEFT, fill=tk.BOTH, padx=8, pady=8)
#                 indexes += 1
#                 sleep(0.5)
#
#     def getting_card(text):
#         card_entry.delete(0, tk.END)
#
#         if new_window.winfo_children() != 1:
#             [x.destroy() for x in new_window.winfo_children()[1:]]
#
#         if text:
#             the_card = cards_info.get_card(text)
#             if the_card:
#                 stuff(the_card)
#                 return
#
#         tk.Label(new_window, text="card not found", bg="grey22", fg="snow", font=("Calibri", 16)).pack()
#
#     searching_frame = tk.Frame(new_window, bg="grey22")
#     searching_frame.pack()
#     card_entry_label = tk.Label(searching_frame, text="Card Name", bg="grey22", fg="snow", font=("Calibri", 13))
#     card_entry_label.pack(side="left")
#     card_entry = tk.Entry(searching_frame, bd=3, bg="grey22", fg="snow", width=50, font=("Calibri", 12))
#     card_entry.pack(side="left",)
#     card_entry.focus_set()
#     card_entry_button = tk.Button(searching_frame,
#                                   text="Confirm", bg="grey22", fg="snow",
#                                   command=lambda: getting_card(card_entry.get()), font=("Calibri", 11))
#     card_entry_button.pack(side="left")
#     card_entry.bind("<Return>", lambda _: getting_card(card_entry.get()))
#     #
#     # card_entry_button.wait_variable(wait)


# class CardAdd:
#     CARDS_PER_FRAME = 5
#
#     def __init__(self):
#         self.new_window = tk.Toplevel(bg="grey22")
#         self.searching_frame = tk.Frame(self.new_window, bg="grey22")
#         self.card_entry_label = tk.Label(self.searching_frame, text="Card Name", bg="grey22", fg="snow", font=("Calibri", 13))
#         self.card_entry = tk.Entry(self.searching_frame, bd=3, bg="grey22", fg="snow", width=50, font=("Calibri", 12))
#         self.card_entry_button = tk.Button(self.searching_frame,
#                                            text="Confirm", bg="grey22", fg="snow",
#                                            command=lambda: self.getting_card(self.card_entry.get()), font=("Calibri", 11))
#
#         self.new_window.minsize(width=1040, height=675)
#         self.searching_frame.pack()
#         self.card_entry_label.pack(side="left")
#         self.card_entry.pack(side="left", )
#         self.card_entry.focus_set()
#         self.card_entry_button.pack(side="left")
#         self.card_entry.bind("<Return>", lambda _: self.getting_card(self.card_entry.get()))
#
#         self.all_images = []
#
#     def getting_card(self, text):
#         self.card_entry.delete(0, tk.END)
#
#         if self.new_window.winfo_children() != 1:
#             [x.destroy() for x in self.new_window.winfo_children()[1:]]
#
#         if text:
#             the_card = cards_info.get_card(text)
#             if the_card:
#                 self.stuff(the_card)
#                 return
#
#         tk.Label(self.new_window, text="card not found", bg="grey22", fg="snow", font=("Calibri", 16)).pack()
#
#     def stuff(self, card):
#         each_variant, amount = each_card_variant(card)
#         each_variant_png = list(each_variant.keys())
#         each_variant_info = list(each_variant.values())
#
#         frames = []
#
#         try:
#             self.new_window.winfo_children()[1].configure(text=f"Variants: {amount}")
#         except Exception:
#             tk.Label(self.new_window, text=f"Variants: {amount}", bg="grey22", fg="snow", font=("Calibri", 16)).pack()
#
#         for _ in range(ceil(amount / self.CARDS_PER_FRAME)):
#             frame = tk.Frame(self.new_window, bg="grey22")
#             frame.pack()
#             frames.append(frame)
#
#         indexes = 0
#
#         for x in frames:
#             for _ in range(self.CARDS_PER_FRAME):
#                 if indexes == len(each_variant_png):
#                     break
#
#                 current_img = each_variant_png[indexes]
#                 current_variant_info = each_variant_info[indexes]
#
#                 response_img = requests.get(current_img)
#                 img_data = response_img.content
#                 img_resize = Image.open(BytesIO(img_data)).resize((182, 247))
#                 img = ImageTk.PhotoImage(img_resize)
#                 self.all_images.append(img)
#
#                 card_button = tk.Button(x, image=img,
#                                         text=f"set: {current_variant_info['set'].upper()}  "
#                                              f"  # {current_variant_info['collector_number']}",
#                                         bd=3, bg="grey12", fg="snow", compound="top", font=("Calibri", 10))
#                 # command=lambda i=indexes: saving_the_card(each_variant_uri[i], new_window)
#                 card_button.pack(side=tk.LEFT, padx=8, pady=8)
#                 indexes += 1
#                 sleep(0.5)


root = tk.Tk()

lol = tk.Button(root, text="add", command=CardAdd)
lol.pack()

root.mainloop()
