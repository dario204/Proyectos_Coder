agenda_1= {}

agenda_1["frodo"]=222
agenda_1["Drogo"]=333

print("Agenda Inicial", agenda_1)

print()



contacto_para_buscar=input("Ingresar el nombre del contacto para buscar:")
telefono=agenda_1.get(contacto_para_buscar.lower, "No encotrado")

print(f"El telefono de {contacto_para_buscar} es:", {telefono})