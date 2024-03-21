

# Ejercicio 1: encapsular el siguiente código en una función
#               y utilizarla para dibujar el tablero 10 veces
"""""
FILAS = 8
COLUMNAS = 10

tablero = []
for i in range(FILAS):
    # fila = []
    # for j in range(COLUMNAS):
    #     fila.append(".")
    fila = ["."] * COLUMNAS  # listas de <COLUMNAS> elementos
    tablero.append(fila)

# tablero tienen <FILAS> elementos
for xx in tablero:
    print("  ".join(xx)) # convertir la lista en str juntada por espacios e imprimirla
 """
def dibujar_tablero():
    FILAS = 8
    COLUMNAS = 10

    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS 
        tablero.append(fila)
        
    tablero[3][4]="0"
    for xx in tablero:
        print("  ".join(xx))

for j in range(10):
    
    dibujar_tablero()
    print()

