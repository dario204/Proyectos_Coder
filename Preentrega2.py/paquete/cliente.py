class Cliente:

    def __init__(self, nombre, apellido, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"El cliente es: {self.nombre} {self.apellido}. Su email es: {self.email}. Y su direccion es {self.direccion} "
    
    def nueva_direccion(self, nueva_direccion):
        self.direccion= nueva_direccion

    

cliente1 = Cliente("Juan", "Perez", "juan@example.com", "Calle 123")


print(cliente1)


cliente1.nueva_direccion("Calle 456")


print("Dirección actualizada:", cliente1.direccion)


