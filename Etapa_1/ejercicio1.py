# Ejercicio 1: Uso de append
# Crea una lista vacía.
# Añade los números del 1 al 5 a la lista utilizando un bucle y el método append.
# Imprime la lista resultante.

lista = []
for i in range(1,6):
    lista.append(i)
print(lista)

# Ejercicio 2: Uso de extend
# Crea una lista con los elementos [1, 2, 3].
# Extiende la lista añadiendo los elementos [4, 5, 6] utilizando el método extend.
# Imprime la lista resultante.

lista = [1,2,3]
lista.extend([4,5,6])
print(lista)

# Ejercicio 3: Uso de count
# Crea una lista con los elementos [1, 2, 2, 3, 3, 3, 4, 4, 4, 4].
# Cuenta cuántas veces aparece el número 3 en la lista utilizando el método count.
# Imprime el resultado.

lista = [1,2,2,3,3,3,4,4,4,4]
contar = lista.count(3)
print(contar)

# Ejercicio 4: Uso de pop
# Crea una lista con los elementos [1, 2, 3, 4, 5].
# Elimina el último elemento de la lista utilizando el método pop.
# Imprime la lista resultante.

lista = [1,2,3,4,5]
lista.pop(4)
print(lista)

# Ejercicio 5: Uso de clear
# Crea una lista con los elementos [1, 2, 3, 4, 5].
# Vacía la lista utilizando el método clear.
# Imprime la lista resultante.

lista = [1,2,3,4,5]
lista.clear()
print(lista)

# Ejercicio 6: Uso de remove
# Crea una lista con los elementos [1, 2, 3, 4, 5].
# Elimina el elemento 3 de la lista utilizando el método remove.
# Imprime la lista resultante.

lista = [1,2,3,4,5]
lista.remove(3)
print(lista)

# Ejercicio 7: Uso de sort
# Crea una lista con los elementos [5, 2, 4, 1, 3].
# Ordena la lista en orden ascendente utilizando el método sort.
# Imprime la lista resultante.

lista = [5,3,2,4,1]
lista.sort()
print(lista)
lista.reverse()
print(lista)

# Ejercicio 8: Uso de index
# Crea una lista con los elementos [10, 20, 30, 40, 50].
# Encuentra el índice del elemento 30 en la lista utilizando el método index.
# Imprime el resultado.

lista = [10,20,30,40,50]
busca = lista.index(30)
print(busca)

# Ejercicio 9: Uso de tuplas
# Crea una tupla con los elementos (1, 2, 3, 4, 5).
# Imprime el segundo elemento de la tupla.
# Intenta modificar el tercer elemento de la tupla y observa qué sucede

tupla = (1,2,3,4,5)
print(tupla[2])
