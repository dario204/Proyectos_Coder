registro = {}

def almacenar_informacion(usuario, contrasenia):
    registro[usuario] = contrasenia

def mostrar_informacion():
    print("Usuario registrado:")
    for usuario, contrasenia in registro.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasenia}")

def login():
    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese su nombre de usuario: ")
        contrasenia = input("Ingrese su contraseña: ")
        if usuario in registro and registro[usuario] == contrasenia:
            print("Inicio de sesión exitoso!")
            break
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
    else:
        print("Has agotado todos los intentos. Por favor, inténtalo más tarde.")

def main():
    # Registro de un usuario al iniciar el programa
    usuario = input("Elegir un nombre de usuario: ")
    contrasenia = input("Elegir una contraseña: ")
    almacenar_informacion(usuario, contrasenia)
    
    # Mostrar el registro antes de continuar
    print("Registro actual:")
    mostrar_informacion()
    print("\nPor favor, inicie sesión.")
    
    # Continuar con el resto del programa
    login()

if __name__ == "__main__":
    main()
