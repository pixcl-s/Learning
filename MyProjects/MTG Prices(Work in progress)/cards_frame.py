import tkinter as tk
import interface
import scroll_frame


class CardsFrame:
    def __init__(self, canvas):
        self.frame = tk.Frame(canvas.scroll_frame, bg="grey22")

    def packing(self):
        self.frame.pack(side="left", fill="both", expand=True)


card_frame_one = CardsFrame(scroll_frame.canvas_frame)
card_frame_one.packing()
# cards_frame_one.frame.configure(bg="grey15")

card_label_one = CardsFrame(scroll_frame.canvas_frame)
card_label_one.packing()
# cards_label_one.frame.configure(bg="grey25")

card_frame_two = CardsFrame(scroll_frame.canvas_frame)
card_frame_two.packing()
# cards_frame_two.frame.configure(bg="grey35")

card_label_two = CardsFrame(scroll_frame.canvas_frame)
card_label_two.packing()
# cards_label_two.frame.configure(bg="grey5")

# card_frame_one = tk.Frame(scroll_frame.canvas_frame.scroll_frame, bg="grey22")
# card_frame_two = tk.Frame(scroll_frame.canvas_frame.scroll_frame, bg="grey22")
# card_label_one = tk.Frame(scroll_frame.canvas_frame.scroll_frame, bg="grey22")
# card_label_two = tk.Frame(scroll_frame.canvas_frame.scroll_frame, bg="grey22")
# card_frame_one.pack(side="left", fill="both", expand=True)
# card_frame_two.pack(side="left", fill="both", expand=True)
# card_label_one.pack(side="left", fill="both", expand=True)
# card_label_two.pack(side="left", fill="both", expand=True)
