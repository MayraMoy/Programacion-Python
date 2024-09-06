import tkinter as tk
from constantes import style
from screens import Home, Game

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Yo Nunca: The Game')
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand=True
        )
        container.configure(background=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
        self.frame = {}
        for F in (Home, Game):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row= 0, column=0, sticky=tk.NSEW)