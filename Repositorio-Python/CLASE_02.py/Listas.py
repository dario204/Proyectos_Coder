mi_Lista=[1, 5, 6, 8,"frodo", "mary" ]
print(mi_Lista[4])

#Calcular Longitud
print("La longitud de mi lista es:", len(mi_Lista))
print("La longitud de mi lista es:", len(mi_Lista[4]))

#Reemplazar 1 Elemento
mi_Lista[3]= "Gandalf"
print("Mi nueva lista es:", mi_Lista)

#Reemplazar 1 elemento con Slicing
mi_Lista[:2]= "Aragon", "Bodomir"
print("Mi nueva lista es:", mi_Lista)

#Concatenar una lista con otra
mi_otra_lista=["Legolas", "Gimli"]
mi_Lista=mi_Lista+mi_otra_lista
print("Mi nueva lista es:",mi_Lista)

#Agregar un elemento
elemento= "Pippin"
mi_Lista.append(elemento)
print("Mi nueva lista es:", mi_Lista)

#Remover 1 elemento
del mi_Lista[2]
print("Mi nueva lista es:", mi_Lista)
