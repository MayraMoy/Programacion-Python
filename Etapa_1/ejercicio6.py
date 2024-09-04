print()
print("Generaciones digitales")
print("----------------------")
print()
print("¿Quieres conocer a que Generacion perteneces?")

Answer = int(input("Ingrese el año en el que nacio: "))

if 1920 <= Answer <= 1940:
    print("Usted pertenece a la Generacion Silenciosa")
elif 1946 <= Answer <= 1964:
    print("Usted pertenece a la Generacion Boomer")
elif 1965 <= Answer <= 1979:
    print("Usted pertenece a la Generacion X")
elif 1980 <= Answer <= 2000:
    print("Usted pertenece a la Generacion Y")
elif 2001 <= Answer <= 2010:
    print("Usted pertenece a la Generacion Z")
else:
    print("No existe generacion")