agenda=["No existe"]*16
agenda[5]= 11234566
agenda[3]= 12344355


print("El telefono de Frodo es:", agenda[5])

print("El telefono de Kiri es:", agenda[10])

################################################################

agenda_1= {}

agenda_1["frodo"]=222
agenda_1["Drogo"]=333

print("Agenda", agenda_1)

print()
print()

nombre= input("Ingrese el nombre:")
telefono=input("Ingrese el telefono:")

agenda_1[nombre]= telefono
print()
print("Agenda actualizada", agenda_1)

contacto_para_buscar=input("Ingresar el nombre del contacto para buscar:")
telefono=agenda_1[contacto_para_buscar]
print("El numero de tu contacto es:",  telefono)
print(f"El telefono de {contacto_para_buscar} es:", telefono) #La f toma el valor de la variable y lo muestra, sin ella se mostraria el nombre de la variable
print(f"El telefono de {contacto_para_buscar} es:", {telefono})