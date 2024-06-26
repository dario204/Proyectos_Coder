class Cliente:

    def __init__(self, nombre, identificador, email):
        self.nombre = nombre
        self.identificador = identificador
        self.email = email


class Persona(Cliente):
    def __init__(self, nombre, documento, edad, email):
        super().__init__(nombre, documento, email)
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}"


class Empresa(Cliente):
    def __init__(self, nombre, identificador, email):
        super().__init__(nombre, identificador, email)
        self.razon_social = nombre

    def __str__(self):
        return f"Empresa: {self.razon_social}"


persona_1 = Persona("alberto", 22123233, 89, "al@berto.com")
empresa_1 = Empresa("Compumundo hipermegared", "20-1312312-12","compumundo@mundo.com")
cliente_1 = Cliente()

print(persona_1)
print(empresa_1)