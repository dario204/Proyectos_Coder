mi_lista = ["Magenta", "Riff Raff", "Columbia", "Rocky"]

f = open("personajes.txt", "w")
f.write(str(mi_lista))
f.close()

f = open("personajes.txt", "r")
contenido= f.read()
f.close()

print(contenido)