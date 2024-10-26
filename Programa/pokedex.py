import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style, Window
import requests
from tkinter import ttk

root = Window(themename="superhero")
base_url = "https://pokeapi.co/api/v2/"

class MostrarPokemon:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokedex")

        self.date_label = ttk.Label(self.root, text="Ingrese el nombre del Pokémon", bootstyle="info")
        self.date_label.pack(padx=40, pady=5)

        self.entry = ttk.Entry(root, width=30, bootstyle="primary")
        self.entry.pack(padx=40, pady=5)

        self.search_button = ttk.Button(root, text="Buscar", bootstyle="success", command=self.get_pokemon_info)
        self.search_button.pack(pady=5)

        self.name_label = ttk.Label(root, text="Nombre: ", font=("Georgia", 12))
        self.name_label.pack(pady=3)

        self.id_label = ttk.Label(root, text="ID: ", font=("Georgia", 12))
        self.id_label.pack(pady=3)

        self.height_label = ttk.Label(root, text="Altura: ", font=("Georgia", 12))
        self.height_label.pack(pady=3)

        self.weight_label = ttk.Label(root, text="Peso: ", font=("Georgia", 12))
        self.weight_label.pack(pady=3)

    def get_pokemon_info(self):
        name = self.entry.get().strip().lower()
        if not name:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre del Pokémon.")
            return

        url = f"{base_url}pokemon/{name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data = response.json()
            self.display_pokemon_info(pokemon_data)
        else:
            messagebox.showerror("Error", f"No se pudo recuperar la información del Pokémon: {name}.")
    
    def display_pokemon_info(self, pokemon_info):
        self.name_label.config(text=f"Nombre: {pokemon_info['name'].capitalize()}")
        self.id_label.config(text=f"ID: {pokemon_info['id']}")
        self.height_label.config(text=f"Altura: {pokemon_info['height'] / 10} m")
        self.weight_label.config(text=f"Peso: {pokemon_info['weight'] / 10} kg")

app = MostrarPokemon(root)
root.mainloop()

