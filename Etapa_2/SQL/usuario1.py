# Importamos sqlite3
import sqlite3
# Importamos tkinter y la renombramos
import tkinter as tk
from tkinter import ttk

# Creamos una funcion para mostrar los usuarios
def mostrar_usuarios():
    # Conectamos con la base de datos
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    
    # Consultamos los usuarios
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    
    # Cerramos la conexion
    conn.close()
    
    # Creamos una ventana principal
    root = tk.Tk()
    root.title('Usuarios')
    
    # Creamos un Treeview para mostrar los datos
    tree = ttk.Treeview(root, columns =('id', 'nombre', 'edad', 'email'), show='headings')
    tree.heading('id', text='id')
    tree.heading('nombre', text='nombre')
    tree.heading('edad', text='edad')
    tree.heading('email', text='email')
    
    # Insertamos los datos en el Treeview
    for usuario in usuarios:
        tree.insert('', 'end', values= usuario)
    
    # Empacamos el Treeviw
    tree.pack(fill='both', expand=True)
    
    # Iniciamos el loop principal de la ventana
    root.mainloop()
    
# LLamamos a la funcion para mostrar los usuarios
mostrar_usuarios()