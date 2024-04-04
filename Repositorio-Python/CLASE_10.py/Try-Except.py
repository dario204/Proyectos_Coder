# Pedir al usuario que ingrese 2 numeros, sumarlos y motrarlos por pantalla
# Si el usuario ingresa algo que no puede ser interpretado como numero
# entonces mostrarle un mensaje de error y pedirle que ingrese números nuevamente

while True:
    try:
        # Pedir al usuario que ingrese dos números
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        
        # Sumar los dos números
        suma = numero1 + numero2
        
        # Mostrar el resultado por pantalla
        print(f"La suma de {numero1} y {numero2} es: {suma}")
        
        # Salir del bucle while si todo es exitoso
    except ValueError:
        # Capturar excepción si el usuario ingresa algo no convertible a número
        print("Error: Ingrese números válidos. Inténtelo nuevamente.")
    else:
        print (numero1+numero2)
        break