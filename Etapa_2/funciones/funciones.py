# Funcion para sumar numeros
def sumar_numero():
    a = int(input('Ingresa un numero: '))
    b = int(input('Ingresa un numero: '))
    c = int(input('Ingresa un numero: '))
    resultado = a + b + c
    print(f'El resultado es: {resultado}')

# Llamando la funcion
sumar_numero()

# Funcion para sumar numeros
def sumar_numeros(a,b,c):
    return a + b + c

# Llamando a la funcion
resultado = sumar_numeros(1,2,3)
print(resultado)

# Funcion para saludar al usuario
def saludar():
    nombre = input('Ingrese su nombre: ')
    print(f'Hola {nombre} bienvenido.')

# Llamando a la funcion
saludar()