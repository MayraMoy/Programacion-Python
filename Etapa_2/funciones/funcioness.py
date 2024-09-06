# La palabra clave def en Python se utiliza para definir una función. 
# Una función es un bloque de código que realiza una tarea específica y puede ser reutilizado en diferentes 
# partes de un programa. 
# Definir una función te permite organizar tu código y evitar la repetición.

def nombre_de_la_funcion(parámetros):
    """Documentación de la función (opcional)."""
    # Cuerpo de la función
    # Código que se ejecutará cuando se llame a la función
    return #valor_de_retorno

# def: Palabra clave para definir una función.
# nombre_de_la_funcion: Nombre que le das a la función.
# parámetros: Variables que la función puede recibir como entrada, separadas por comas.
# """Documentación""": Una cadena opcional que describe la función.
# return: Palabra clave para devolver un valor desde la función (opcional).

# Ejemplo 1: Función sin Parámetros
def saludar():
    """Esta función imprime un saludo."""
    print("¡Hola!")

# Llamar a la función
saludar()

# Ejemplo 2: Función con Parámetros
def saludar(nombre):
    """Esta función saluda a la persona cuyo nombre se pasa como parámetro."""
    print(f"¡Hola, {nombre}!")

# Llamar a la función con un parámetro
saludar("David")

# def: Esta palabra clave se utiliza para definir una nueva función en Python.
# saludar: Es el nombre que se le da a la función. Puedes llamarla así para ejecutar su código.
# (nombre): Esto indica que la función saludar acepta un argumento (o parámetro) llamado nombre. 
# Cuando llames a esta función, deberás pasarle un valor que será asignado a nombre.
# f"¡Hola, {nombre}!": Esta es una cadena formateada (f-string).
# El prefijo f permite insertar variables directamente en la cadena. {nombre} se reemplaza con el 
# valor del argumento que se pasa cuando se llama a la función.
# Por ejemplo, si llamas a saludar("David"), se imprimirá ¡Hola, David!.
# Llama a la función saludar.
# Asigna el valor "David" al parámetro nombre.
# Ejecuta el código dentro de la función, lo que resulta en la impresión de ¡Hola, David!.


# Ejemplo 3: Función con Parámetros y Valor de Retorno

def sumar(a, b):
    """Esta función retorna la suma de dos números."""
    return a + b

# Llamar a la función y almacenar el valor de retorno en una variable
resultado = sumar(3, 5)
print(resultado)  # Imprime 8


# def: Esta palabra clave se utiliza para definir una nueva función en Python.
# sumar: Es el nombre que se le da a la función. Este nombre se usará para llamar a la función en el programa.
# (a, b): Estos son los parámetros que la función aceptará. a y b son variables que representarán los dos números que se van a sumar.
# return: Esta palabra clave se usa para devolver un valor desde la función. 
# Cuando se llama a la función, el resultado de esta línea se puede utilizar en otros lugares.
# a + b: Aquí se realiza la suma de los dos parámetros. El resultado de esta operación se devolverá al lugar donde se llamó a la función.