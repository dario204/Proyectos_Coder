#Ejercicio 1

#def calcular_factorial(n):
 #   if n==0:
  #      return 1
   # else:
    #    return n * calcular_factorial(n - 1)

#resultado= calcular_factorial(4)
#print("El factorial de 4 es: " ,(resultado))

def factorial(numero: int):
    resultado = 1
    while numero > 0:
        resultado=resultado*numero
        numero-=1
    return resultado