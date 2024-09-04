# Aqui creamos una variable llamada "Nombre" a la cual por consola le pediremos al usuario ingresar su nombre y 
# a raiz de ese dato le daremos un saludo mas personalizado
Nombre = input("Ingrese su nombre ")
print("Hola", Nombre)

# Declarar variables
edad = 20 # para declarar una variable solo usamos el "="
x,y,z = 20,30,40 # otra forma de declarar varias variables es creando la misma cantidad de variables que de datos que guardaremos
print(z,y,x) # para visualizar

# Creamos la variable "num" donde pediremos al usuario ingresar numeros
num = int (input("Ingrese un numero "))
num1 = int (input("Ingrese el segundo numero "))
resultado = (num * num1)
print(resultado)

edad = int(input("¿Que edad tienes? "))
print("tu edad es: ")
print(edad)
print(type(edad))