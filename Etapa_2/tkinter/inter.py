# Importamos la libreria Tkinter y la renombramos tk
import tkinter as tk
# Dentro de la libreria Tkinter importamos el modulo de "simpledialog" que son dialogos de entrada estandar
# y messagebox es un modulo que permite crear cuadros de mensaje y dialogos para confitmar o rechazar acciones
from tkinter import simpledialog, messagebox  

#crear la ventana principal
# root se utiliza para nombrar a la ventana principal de la aplicacion, tambien conocida como ventana raiz
root=tk.Tk()
root.title("lista de nombres")
# establece la posición y las dimensiones de la ventana principal
root.geometry("400x300") #tamaño de la ventana
#lista para almacenar los nombres
nombres = []

#funcion para agregar nombres
def agregar_nombre():
    nuevo_nombre=simpledialog.askstring("agregar nombre", "ingrese el nombre:")
    if nuevo_nombre:
        nombres.append (nuevo_nombre)
        actualizar_text ()

#funcion para actualizar nombre
def actualizar_text ():
    text_nombres.delete (1.0, tk.END) #limpia el texto
    for nombre in nombres:
        text_nombres.insert(tk.END, nombre + "\n") #alt+92 para la barra invertida \


#funcion para eliminar nombre
def eliminar_nombre():
    seleccion = text_nombres.index (tk.INSERT). split ('.')[0] # 0btener la linea seleccionada.
    if seleccion and int(seleccion)<=len(nombres):
        del nombres [int(seleccion)-1]#eliminar el nombre de la lista
        actualizar_text()
    else: # El módulo messagebox de tkinter es un módulo que permite crear cuadros de mensaje de información predeterminados.
        messagebox.showwarning("advertencia","seleccione un nombre para eliminar")
        
#funcion para modificar nombre
def modificar_nombre():
    seleccion = text_nombres.index (tk.INSERT). split ('.')[0] # 0btener la linea seleccionada.
    if seleccion and int(seleccion)<=len(nombres):
        nombre_actual= nombres[int(seleccion)-1]
        nuevo_nombre=simpledialog.askstring ("modificar nombre", f"modificar el nombre({nombre_actual})")
        if nuevo_nombre:
            nombres[int(seleccion)-1] = nuevo_nombre
            actualizar_text()
        else:
            messagebox.showwarning("advertencia","seleccione un nombre para modificar: ")
        
#crear el texto para mostrar los nombres
text_nombres=tk.Text (root,width=50, height= 10, bg="lightblue", fg="black", font =("arial", 12))
text_nombres.pack (pady=20)

#crear los botones para agregar, modificar y eliminar
boton_agregar=tk.Button(root, text ="agregar nombre", command=agregar_nombre)
boton_agregar.pack(pady=20)

boton_eliminar=tk.Button(root, text ="eliminar nombre", command=eliminar_nombre)
boton_eliminar.pack(pady=20)

boton_modificar=tk.Button(root, text ="modificar nombre", command=modificar_nombre)
boton_modificar.pack(pady=20)

#iniciar el bucle principal de la ventana
root.mainloop()