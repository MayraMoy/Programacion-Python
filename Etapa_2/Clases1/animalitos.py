class Animal:
    def __init__(self, nombre):
        self.nombre = nombre


class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} hace ¡Guau, Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} hace ¡Miau, Miau!"

perro = Perro("Simon")
gato = Gato("Goku")

print(perro.hacer_sonido())  
print(gato.hacer_sonido())   

class Vehiculos:
    def __init__(self, marca):
        self.nombre = marca

class Bicicleta(Vehiculos):
    def informar_tipo(self):
        return f"{self.marca} el tipo de orquillas es {self}"

bici = Bicicleta()