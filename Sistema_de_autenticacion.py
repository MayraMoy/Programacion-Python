import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.geometry("300x250")
app.configure(background="white")
app.title('Sistema de Autenticación')

usuario_correcto = "mayra25"
contraseña_correcta = 1234
intentos = 3

# Funciones para la interfaz
def Usuario():
    global intentos
    nombre = entry_usuario.get()
    if nombre == usuario_correcto:
        Contraseña()
    else:
        intentos -= 1
        messagebox.showwarning("Error", f"Nombre de usuario incorrecto. Te quedan {intentos} intentos.")
        if intentos == 0:
            bloquear()

def Contraseña():
    global intentos
    try:
        contraseña = int(entry_contraseña.get())
        if contraseña == contraseña_correcta:
            messagebox.showinfo("Acceso", "¡Acceso concedido!")
        else:
            intentos -= 1
            messagebox.showwarning("Error", f"Contraseña incorrecta. Te quedan {intentos} intentos.")
            if intentos == 0:
                bloquear()
    except ValueError:
        messagebox.showerror("Error", "La contraseña debe ser un número.")

def bloquear():
    entry_usuario.config(state="disabled")
    entry_contraseña.config(state="disabled")
    btn_login.config(state="disabled")
    messagebox.showerror("Bloqueo", "Has superado el número máximo de intentos. Acceso denegado.")

# Elementos de la interfaz
label_usuario = tk.Label(app, text="Usuario:", bg="white")
label_usuario.pack(pady=10)
entry_usuario = tk.Entry(app)
entry_usuario.pack(pady=5)

label_contraseña = tk.Label(app, text="Contraseña:", bg="white")
label_contraseña.pack(pady=10)
entry_contraseña = tk.Entry(app, show="*")
entry_contraseña.pack(pady=5)

btn_login = tk.Button(app, text="Iniciar Sesión", command=Usuario)
btn_login.pack(pady=20)

# Iniciar la aplicación
app.mainloop()
