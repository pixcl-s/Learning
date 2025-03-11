import tkinter


def window_base():
    root = tkinter.Tk()
    root.title("Appage")
    root.geometry("600x400")
    return root


start = window_base()
start.configure(background="grey14")
