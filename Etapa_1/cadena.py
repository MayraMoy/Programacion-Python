# La funcion len sirve para contar los caracteres de una cadena
palabra = "Python"
print(len(palabra))

frase = "Hola, ¿como estan? ¡Yo bien!"
print(len(frase))

# Buscamos en la cadena lo que se encuentra en el espacio 5
cadena = "Python"
cadena [0]
cadena [-1]
print(cadena[5])

# Concatenar cadenas
numeros = [1,2,3,4] 
numeros += [5,6,7,8]
print (numeros)

datos = [1,-5,123,34,"una cadena","otra cadena"]
datos += [0,"otra cadena distinta", "pepito", 450, 86]
print (datos)

# Cambiamos lo que se encuentra en el espacio 3 por el numero 6
pares = [0,2,4,5,8,10]
pares [3] = 6
print (pares)

# Agregamos un elemento a la lista
numeros = [1,2,3,4]
numeros.append(5)
print(numeros)

# Borramos el elemento que se encuentre en el espacio 3
numeros = [1,2,3,4]
numeros.pop(3)
print (numeros)

# contamos cuantas veces se repite el elemento
numeros = [1,2,1,3,1,4,1]
print (numeros.count(1))
