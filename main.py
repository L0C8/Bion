from tkinter import Tk
from gui.gui import BionApp
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

if __name__ == "__main__":
    root = Tk()
    app = BionApp(root)
    root.mainloop()
