import tkinter as tk
from tkinter import ttk
import ttkbootstrap

class CalendarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendario")
        self.eventos = {}  
        
        
        self.cal = ttkbootstrap.DateEntry(self.root, dateformat='%d/%m/%Y', bootstyle="info")
        self.cal.pack(padx=40, pady=10)
        
        self.date_label = ttk.Label(self.root, text="Ninguna fecha seleccionada")
        self.date_label.pack(padx=40, pady=5)
        
        self.evento_label = ttk.Label(self.root, text="Descripción del evento")
        self.evento_label.pack(padx=40, pady=5)
        
        self.evento_entry = ttk.Entry(self.root, width=30)
        self.evento_entry.pack(padx=40, pady=5)
        
        self.btn_agregar = ttk.Button(self.root, text="Agregar Evento", bootstyle="success", command=self.agregar_evento)
        self.btn_agregar.pack(padx=40, pady=5)
        
        self.btn_eliminar = ttk.Button(self.root, text="Eliminar Evento", bootstyle="danger", command=self.eliminar_evento)
        self.btn_eliminar.pack(padx=40, pady=5)
        
        self.btn_mostrar = ttk.Button(self.root, text="Mostrar Fecha", bootstyle="light-outline", command=self.see_date)
        self.btn_mostrar.pack(padx=40, pady=10)
        
        self.eventos_listbox = tk.Listbox(self.root, width=40, height=10)
        self.eventos_listbox.pack(padx=40, pady=10)
        
    def see_date(self):
        date = self.cal.entry.get()
        self.date_label.config(text=f"Fecha seleccionada: {date}")
        self.mostrar_eventos(date)

    def agregar_evento(self):
        date = self.cal.entry.get()
        evento = self.evento_entry.get()
        if date and evento:
            if date in self.eventos:
                self.eventos[date].append(evento)
            else:
                self.eventos[date] = [evento]
            self.evento_entry.delete(0, tk.END)
            self.mostrar_eventos(date)

    def eliminar_evento(self):
        date = self.cal.entry.get()
        selected_evento = self.eventos_listbox.curselection()
        if date in self.eventos and selected_evento:
            evento = self.eventos_listbox.get(selected_evento)
            self.eventos[date].remove(evento)
            if not self.eventos[date]:  
                del self.eventos[date]
            self.mostrar_eventos(date)

    def mostrar_eventos(self, date):
        self.eventos_listbox.delete(0, tk.END)  
        if date in self.eventos:
            for evento in self.eventos[date]:
                self.eventos_listbox.insert(tk.END, evento)


root = ttkbootstrap.Window(themename="cyborg")
app = CalendarioApp(root)
root.mainloop()
