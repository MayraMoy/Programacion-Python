import tkinter as tk

app = tk.Tk()
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)
app.geometry("300x600") #Acho por alto
app.configure(background="black") # Ahora el fondo pasara a ser de color negro
tk.Wm.wm_title(app, 'Hola Bienvenido')

def cambiar_Palabra():
    palabra.set('Soy gay ' + entrada.get())
tk.Button(
    app, 
    text= "Click!",
    font=("Courie'", 14),
    bg= '#00a8e8',
    fg='white',
    command= cambiar_Palabra,
    relief='flat'
).pack(
    fill=tk.BOTH,
    expand=True,
)

tk.Label(
    app,
    text='Escribe algo aqui abajo',
    textvariable=palabra,
    fg='white',
    bg='black',
    justify='center',
).pack(
    fill=tk.BOTH,
    expand=True,
)

tk.Entry(
    fg='white',
    bg='black',
    justify='center',
    textvariable=entrada,
).pack(
    fill=tk.BOTH,
    expand=True,
)
app.mainloop()