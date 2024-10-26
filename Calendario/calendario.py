import tkinter as tk 
from tkinter import ttk 
import ttkbootstrap 

root = ttkbootstrap.Window(themename="cyborg") 
root.title("Calendario")  

eventos = {} 

def see_date(): 
    date = cal.entry.get() 
    date_label.config(text=f"Fecha seleccionada: {date}") 
    mostrar_eventos(date) 

def agregar_evento(): 
    date = cal.entry.get() 
    evento = evento_entry.get() 
    if date and evento: 
        if date in eventos: 
            eventos[date].append(evento) 
        else:
            eventos[date] = [evento] 
        evento_entry.delete(0, tk.END) 
        mostrar_eventos(date) 

def eliminar_evento(): 
    date = cal.entry.get() 
    selected_evento = eventos_listbox.curselection() 
    if date in eventos and selected_evento: 
        evento = eventos_listbox.get(selected_evento) 
        eventos[date].remove(evento) 
        if not eventos[date]:  
            del eventos[date] 
        mostrar_eventos(date) 

def mostrar_eventos(date): 
    eventos_listbox.delete(0, tk.END)  
    if date in eventos: 
        for evento in eventos[date]: 
            eventos_listbox.insert(tk.END, evento)  


cal = ttkbootstrap.DateEntry(root, dateformat='%d/%m/%Y', bootstyle="info")
cal.pack(padx=40, pady=10)

date_label = ttk.Label(root, text="Ninguna fecha seleccionada")
date_label.pack(padx=40, pady=5)

evento_label = ttk.Label(root, text="Descripción del evento")
evento_label.pack(padx=40, pady=5)

evento_entry = ttk.Entry(root, width=30)
evento_entry.pack(padx=40, pady=5)

btn_agregar = ttk.Button(root, text="Agregar Evento", bootstyle="success", command=agregar_evento)
btn_agregar.pack(padx=40, pady=5)

btn_eliminar = ttk.Button(root, text="Eliminar Evento", bootstyle="danger", command=eliminar_evento)
btn_eliminar.pack(padx=40, pady=5)

btn_mostrar = ttk.Button(root, text="Mostrar Fecha", bootstyle="light-outline", command=see_date)
btn_mostrar.pack(padx=40, pady=10)

eventos_listbox = tk.Listbox(root, width=40, height=10)
eventos_listbox.pack(padx=40, pady=10)

root.mainloop()
