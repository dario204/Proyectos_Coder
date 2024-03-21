ruta_del_archivo = "archivo.txt"

f = open(ruta_del_archivo, "r")
contenido = f.read()
f.close()
print()

f = open(ruta_del_archivo, "r")
contenido = f.readline()
f.close()

for line in contenido:
   print(line)

