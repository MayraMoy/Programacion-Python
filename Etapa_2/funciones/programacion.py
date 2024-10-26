# Se crea una funcion que en el caso de no ingresar un nombre dira 'Hola, invitado'
def saludar(nombre=None):
    if nombre is None:
        print("Hola, invitado!")
    else:
        print(f"Hola, {nombre}!")

def sumar(a, b):  # a y b son los parámetros
    return a + b
resultado = sumar(3, 5)
print(resultado)

# Ejemplo 1: Función sin Parámetros
def saludar():
    """Esta función imprime un saludo."""
    print("¡Hola!")

# Ejemplo 2: Función con Parámetros
def saludar(nombre):
    """Esta función saluda a la persona cuyo nombre se pasa como parámetro."""
    print(f"¡Hola, {nombre}!")

# Ejemplo 4: Función con Parámetros Predeterminados
def saludar(nombre="amigo"):
    """Esta función saluda a la persona cuyo nombre se pasa como parámetro.
    Si no se pasa un nombre, saluda a 'amigo' por defecto."""
    print(f"¡Hola, {nombre}!")

def registrar_estudiante(estudiantes, id_estudiante, nombre, edad, grado):
    estudiante = {
        "ID": id_estudiante,
        "Nombre": nombre,
        "Edad": edad,
        "Grado": grado
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito!")

registrar_estudiante()

