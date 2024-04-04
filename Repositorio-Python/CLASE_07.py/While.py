# 2. Modificar el ejercicio anterior para que:
#   a. j nunca sea mayor que 4.
#   b. j asuma los valores 0, 1, 2, y 3 infinitas veces
import time
j = 0
while j < 4:
    time.sleep(1)
    print(f"j vale: {j}")
    j += 1
    if j== 4:
        j=0