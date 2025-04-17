import tkinter as tk
import interface


class CanvasFrame:
    def __init__(self, main):
        # super().__init__(main)

        self.canvas = tk.Canvas(main.root, bg="grey22")
        self.scrollbar = tk.Scrollbar(main.root, bg="snow", trough="grey1", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scroll_frame = tk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame)
        self.scroll_frame.bind("<Configure>", self.frame_configure)
        self.canvas.bind("<Configure>", self.frame_resize)

    def grid(self):
        self.canvas.grid(row=1, column=0, sticky="nesw")
        self.scrollbar.grid(row=1, column=1, sticky="nse")

    def frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def frame_resize(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)


canvas_frame = CanvasFrame(interface.app)
canvas_frame.grid()

