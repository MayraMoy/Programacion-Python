import sqlite3
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk


conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos(
        id_Producto INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Precio INTEGER,
        Categoria TEXT
    )
''')
conn.commit()

app = tk.Tk()
app.title("Sistema de Gestion")
app.geometry("900x600")


etiqueta = ttk.Label(app,
                    text="CAFETERIA",
                    font=("Arial Black", 30),
                    foreground="Dark Orange",
                    padding=(20, 10),
                    anchor="center")
etiqueta.pack(pady=40)

class Cafeteria:
    def __init__(self, root):
        self.root = root

        frame_botones = ttk.Frame(app)
        frame_botones.pack(pady=20)

        self.boton_mostrar = ttk.Button(frame_botones, text="Mostrar Productos", command=self.mostrar_Productos)
        self.boton_mostrar.pack(side=tk.LEFT, padx=10)

        self.boton_agregar = ttk.Button(frame_botones, text="Agregar Producto", command=self.agregar_Producto)
        self.boton_agregar.pack(side=tk.LEFT, padx=10)

        self.boton_modificar = ttk.Button(frame_botones, text="Modificar Producto", command=self.modificar_Producto)
        self.boton_modificar.pack(side=tk.LEFT, padx=10)

        self.boton_eliminar = ttk.Button(frame_botones, text="Eliminar Producto", command=self.eliminar_producto)
        self.boton_eliminar.pack(side=tk.LEFT, padx=10)

        self.lista_productos = tk.Listbox(app, width=50, height=10)
        self.lista_productos.pack(pady=20)
        self.mostrar_Productos()

    def mostrar_Productos(self):
        conn = sqlite3.connect('mi_base_de_datos.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()

        self.lista_productos.delete(0, tk.END)

        for producto in productos:
            texto_producto = f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Categoría: {producto[3]}"
            self.lista_productos.insert(tk.END, texto_producto)

        conn.close()

    def agregar_Producto(self):
        def guardar_Producto():
            nombre = entrada_nombre.get()
            precio = entrada_precio.get()
            categoria = entrada_categoria.get()

            if nombre and precio and categoria:
                try:
                    precio = int(precio)
                    cursor.execute("INSERT INTO Productos (Nombre, Precio, Categoria) VALUES (?, ?, ?)", (nombre, precio, categoria))
                    conn.commit()
                    messagebox.showinfo("Éxito", "Producto agregado correctamente.")
                    ventana_agregar.destroy()
                    self.mostrar_Productos()
                except ValueError:
                    messagebox.showerror("Error", "El precio debe ser un número entero.")
            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        ventana_agregar = tk.Toplevel(app)
        ventana_agregar.title("Agregar Producto")

        etiqueta_nombre = tk.Label(ventana_agregar, text="Nombre:")
        etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5)

        entrada_nombre = tk.Entry(ventana_agregar)
        entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        etiqueta_precio = tk.Label(ventana_agregar, text="Precio:")
        etiqueta_precio.grid(row=1, column=0, padx=5, pady=5)

        entrada_precio = tk.Entry(ventana_agregar)
        entrada_precio.grid(row=1, column=1, padx=5, pady=5)

        etiqueta_categoria = tk.Label(ventana_agregar, text="Categoría:")
        etiqueta_categoria.grid(row=2, column=0, padx=5, pady=5)

        entrada_categoria = tk.Entry(ventana_agregar)
        entrada_categoria.grid(row=2, column=1, padx=5, pady=5)

        boton_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar_Producto)
        boton_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def modificar_Producto(self):
        try:
            producto_seleccionado = self.lista_productos.get(tk.ANCHOR)
            id_producto = producto_seleccionado.split(",")[0].split(":")[1].strip()

            def actualizar_Producto():
                nombre = entrada_nombre.get()
                precio = entrada_precio.get()
                categoria = entrada_categoria.get()

                if nombre and precio and categoria:
                    try:
                        precio = int(precio)
                        cursor.execute("UPDATE Productos SET Nombre=?, Precio=?, Categoria=? WHERE id_Producto=?", (nombre, precio, categoria, id_producto))
                        conn.commit()
                        messagebox.showinfo("Éxito", "Producto modificado correctamente.")
                        ventana_modificar.destroy()
                        self.mostrar_Productos()
                    except ValueError:
                        messagebox.showerror("Error", "El precio debe ser un número entero.")
                else:
                    messagebox.showerror("Error", "Por favor, complete todos los campos.")

            ventana_modificar = tk.Toplevel(app)
            ventana_modificar.title("Modificar Producto")

            etiqueta_nombre = tk.Label(ventana_modificar, text="Nombre:")
            etiqueta_nombre.grid(row=0, column=0, padx=5, pady=5)

            entrada_nombre = tk.Entry(ventana_modificar)
            entrada_nombre.grid(row=0, column=1, padx=5, pady=5)
            entrada_nombre.insert(0, producto_seleccionado.split(",")[1].split(":")[1].strip())

            etiqueta_precio = tk.Label(ventana_modificar, text="Precio:")
            etiqueta_precio.grid(row=1, column=0, padx=5, pady=5)

            entrada_precio = tk.Entry(ventana_modificar)
            entrada_precio.grid(row=1, column=1, padx=5, pady=5)
            entrada_precio.insert(0, producto_seleccionado.split(",")[2].split(":")[1].strip())

            etiqueta_categoria = tk.Label(ventana_modificar, text="Categoría:")
            etiqueta_categoria.grid(row=2, column=0, padx=5, pady=5)

            entrada_categoria = tk.Entry(ventana_modificar)
            entrada_categoria.grid(row=2, column=1, padx=5, pady=5)
            entrada_categoria.insert(0, producto_seleccionado.split(",")[3].split(":")[1].strip())

            boton_guardar = tk.Button(ventana_modificar, text="Guardar", command=actualizar_Producto)
            boton_guardar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        except IndexError:
            messagebox.showerror("Error", "Por favor, seleccione un producto para modificar.")

    def eliminar_producto(self):
        try:
            producto_seleccionado = self.lista_productos.get(tk.ANCHOR)
            id_producto = producto_seleccionado.split(",")[0].split(":")[1].strip()

            if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este producto?"):
                cursor.execute("DELETE FROM Productos WHERE id_Producto=?", (id_producto,))
                conn.commit()
                self.mostrar_Productos()
        except IndexError:
            messagebox.showerror("Error", "Por favor, seleccione un producto para eliminar.")

cafeteria = Cafeteria(app)
app.config(bg="white")
app.mainloop()