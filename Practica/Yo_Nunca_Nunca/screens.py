import tkinter as tk
from constantes import style

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.game_mode = tk.StringVar(self, value="Normal")
        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text= 'Yo Nunca Nunca',
            justify= tk.CENTER
            )
    

class Game(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
