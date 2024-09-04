#Ejercicio 1: Comparacion de numeros
print()
print("¿Mayor o Menor?")
num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(num < num2)
print()

#Ejercicio 2: Verificación de par o impar
print()
print("Verifica si tu numero es PAR o IMPAR")
print()
num1 = int(input("Ingresa un numero: "))
if num1 % 2 == 0:
    print("Tu numero es par")
else:
    print("Tu numero es impar")

#Ejercicio 3: Determinar si un número es positivo, negativo o cero  
print()
print("Determina si tu numero es positivo, negativo o cero")
print()
numero = int(input("Ingrese un numero: "))
if numero > 0:
    print("Tu numero es positivo")
elif numero < 0:
    print("Tu numero es negativo")
else:
    print("Tu numero es 0")

#Ejercicio 4: Verificación de edad para ingresa bar
print()
print("Veremos si podes pasar al bar o no")
edad = int(input("Ingrese su edad"))
if edad > 18:
    print("Usted si puede ingresar al bar")
else:
    print("Usted es menor, no puede ingresar")

# Ejercicio 5: Categorización de edades  
print()
print("Categorizacion de edades")
edad1 = int(input("Ingrese su edad"))
if 0 <= edad1 <= 13:
    print("Usted es un infante")
elif 13 <= edad1 <= 17:
    print("Usted es un adolescente")
elif 18 <= edad1 <=35:
    print("Usted es un adulto joven")
elif 35 <= edad1 <= 64:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")

#Ejercicio 6: Acceso y modificación de elementos en lista
print()
listaDeCompras = ["Azucar", "Harina", "Miel", "Huevos", "Leche", "Arroz"]
listaDeCompras.pop(2)
listaDeCompras.insert(2, "Cacao")
print(listaDeCompras)

#Ejercicio 7: Concatenación de tuplas 
Anuales = ("Elementos de Matematica y Logica", "Sistemas y Organizaciones", "Programacion", "Base de Datos")
Cuatrimestre1= ("Competencias Comunicacionales", "Aproximacion al Mundo del Trabajo")
Etapa1= Anuales + Cuatrimestre1
print(Etapa1)