registro = {}

def registrar():
    print()
    usuario = input("Elegir un nombre de usuario: ")
    contrasenia = input("Elegir una contraseña: ")
    registro[usuario] = contrasenia
    print("Registro completo.")

def login():
    print()
    print("Inicie sesión.")
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contrasenia = input("Ingrese su contraseña: ")
        if usuario in registro and registro[usuario] == contrasenia:
            print("Inicio de sesión exitoso")
            print()
            break
        else:
            intentos -= 1
            print()
            print(f"Usuario y/o contaseña incorrectos. Tiene {intentos} intentos restantes.")
            print()
    else:
        print("Limite de intentos alcanzado. Intente de nuevo más tarde.")

registrar()
login()

