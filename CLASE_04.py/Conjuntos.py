lista_funciones_ejecutadas=["print","print", "print", "print", "type", "type", "len"]
conjunto_funciones_ejecutadas= set(["print" ,"print" ,"print" ,"type" ,"type" ,"len"])

lista=[1,1,1,1,1,1,1,1,1,2,2,3,3,]
conjunto={1,1,1,1,1,2,2,2,3,3,3,}
print()
print("Lista  ", lista_funciones_ejecutadas)
print("Conjunto  ", conjunto_funciones_ejecutadas)
print()

#Agregar
conjunto.add(6)
conjunto.add(7)
conjunto.add("Frodo")
conjunto.update("[Sam,Pipin]")
print("1   " ,conjunto)

#Remover
conjunto.remove(7)
print("2   ","Removi el 7", conjunto)

#Discard
conjunto.discard("gandalf")
conjunto.discard("1")
print("3    ", conjunto)

#IN
print("Esta el 99 en mi lista?",99 in lista)
print("Esta el 1 en mi conjuntos" ,1 in conjunto)

#POP (Saca aleatoriamente)
elemento=conjunto.pop()
print("5   ","Elemento al azar:", elemento)
print("5   ","El conjunto:", conjunto)