# Descripción de la actividad.

# 1. Para aprobar un crédito, el cliente debe ser mayor de edad.
# 2. Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y
# un ingreso mayor a 2500 dólares.
# 3. En caso no tenga la antigüedad suficiente su ingreso mensual debe ser como mínimo 4000 dólares.
# 4. Si no cumple ninguna de las condiciones, no se aprueba el crédito

# Datos iniciales
edad = int(input("Ingresar edad:"))
antigüedad = int(input("Ingresar antiguedad:"))
ingreso = int(input("Ingresar ingresos totales:"))

if edad >= 18 and antigüedad >= 3 and ingreso >=2500:
    print("Credito aprobado")
else:
    print("Credito desaprobado")