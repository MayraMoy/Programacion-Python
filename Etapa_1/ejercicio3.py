#Clasificar una calificación

print()
print("Clasificar una calificacion")
Clasificacion = float(input("Ingrese su calificacion del 1-10: "))

if 4 <= Clasificacion < 7:
    print("Aprobaste")
elif 7 <= Clasificacion <= 10:
    print("Promocionaste")
else:
    print("Desaprobaste")

print("---------------------------------------------------------")

#Determinar la mayor de tres números

print()
print("Determinar cual es el mayor")
num = int(input("Ingrese el primer numero: "))
num1 = int(input("Ingrese el segundo numero: "))
num2 = int(input("Ingrese el tercer numero: "))

if num > num1 and num > num2:
    print(f"El numero mayor es {num}")
elif num1 > num and num1 > num2:
    print(f"El numero mayor es {num1}")
else:
    print(f"El numero mayor es {num2}")

print("---------------------------------------------------------")

#Clasificar un triángulo por sus lados

print()
print("Clasificar un triangulo")
lado = float(input("Ingrese la longitud del primer lado: "))
lado1 = float(input("Ingrese la longitud del segundo lado: "))
lado2 = float(input("Ingrese la longitud del tercer lado: "))

if lado == lado1 == lado2:
    print("El triangulo es equilatero")
elif lado == lado1 or lado == lado2 or lado1 == lado2:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")

print("---------------------------------------------------------")

#Calculadora
print()
print("Calculadora")
dato = float(input("Ingrese el primer numero: "))
dato1 = float(input("Ingrese el segundo numero: "))
operacion = int(input("Ingrese el numero del tipo de operacion que desea hacer: 1- Suma; 2- Resta; 3- Multiplicacion; 4- Division: "))

if operacion == 1:
    print(f"El resultado es: {dato + dato1}")
elif operacion == 2:
    print(f"El resultado es: {dato - dato1}")
elif operacion == 3:
    print(f"El resultado es: {dato ** dato1}")
else:
    print(f"El resultado es: {dato / dato1}")

print()
