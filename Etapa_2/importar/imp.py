# Importamos un modulo propiamente de python
import datetime
import math

# Creamos una variable con el valor de la fecha actual
x = datetime.datetime.now()
print(x) # Nos mostrara la fecha y hora actual

print()
x = datetime.datetime(2018,6,1)
print(x.strftime("%B")) # Nos muestra el mes

print()
x = math.ceil(1.4) # Redondea al entero mas cercano hacia arriba
y = math.floor(1.4) # Redondea al entero mas cercano hacia abajo
print(x) # Salida 2
print(y) # Salida 1