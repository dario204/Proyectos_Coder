Nombre= input("Ingresar nombre:")
Edad= int(input("Ingresar edad:"))

print(f"Ingresaste {Nombre} y {Edad}")

mi_booleano= (Nombre != "****" 
              and Edad> 5 
              and Edad < 20
              and len(Nombre) >= 4 
              and len(Nombre)<=8)