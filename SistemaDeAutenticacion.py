print()
print("Sistema de Autenticacion")
def verificar_Usuario (usuario, intentos):
    while intentos > 0:
        usuario_ingresado = input("Ingrese su nombre de usuario: ")
        if usuario_ingresado == usuario:
            return True
        else:
            intentos -=1
            print(f"Usuario incorrecto. Le quedan {intentos} intentos, vuelva a intentarlo.")
    return False

def verificar_Contraseña (contraseña, intentos):
    while intentos > 0:
        try:
            contraseña_ingresada = int(input("Ingrese su contraseña: "))
            if contraseña_ingresada == contraseña:
                return True
            else:
                intentos -=1
            print(f"Contraseña incorrecta. Le quedan {intentos} intentos, vuelva a intentarlo.")
        except ValueError:
            print("La contraseña esta compuesta por numeros")
            intentos -= 1
    return False

def Usuario():
    usuario = "mayra25"
    contraseña = 1234
    intentos = 3
    
    if verificar_Usuario(usuario, intentos):
        if verificar_Contraseña (contraseña, intentos):
            print("¡Acceso concedido!")
            print()
            print("Ingresando...")
        else:
            print("Has superado el número máximo de intentos de contraseña. Acceso denegado.")
    else:
        print("Has superado el número máximo de intentos de usuario. Acceso denegado.")

Usuario()