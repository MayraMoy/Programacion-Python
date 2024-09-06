import tkinter as tk
from constantes import style

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller

class Game(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller