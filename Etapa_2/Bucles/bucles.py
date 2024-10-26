# Un bucle es una estructura de control que permite repetir una serie de instrucciones 
# mientras que cumpla con la condicion.

# En este caso i = 1 y en la condicion estamos diciendo que mientras i sea menor que 6, se podra
# ejecutar el bucle. El bucle en este caso se va incrementar en 1 (i += 1)
i = 1
while i < 6:
    print(i)
    i += 1 # Salida [1,2,3,4,5]

print()
# Bueno en este caso estamos pidiendo que haga lo mismo que en el anterior ejercicio solo que
# con una nueva condicion. Y es que mientras i sea igual a 3 entonces frena el bucle.
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1 # Salida [1,2,3]

print()