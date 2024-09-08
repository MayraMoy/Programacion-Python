# Importamos la libreria tkinter y la renombramos
import tkinter as tk
# importamos de la carpeta Constantes e imprtamos el modulo style
from constantes import style
# importamos el modulo screens e importamos la clase Home y Game
from screens import Home, Game

# Creamos la clase Manager
class Manager(tk.Tk):
    # Defino una funcion 
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
        self.show_frame(Home)
    
    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()