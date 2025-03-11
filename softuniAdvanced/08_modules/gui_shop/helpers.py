from ui_base import start


def screen_cleaner():
    for x in start.grid_slaves():
        x.destroy()