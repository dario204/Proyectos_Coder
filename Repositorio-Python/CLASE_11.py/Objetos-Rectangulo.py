class Rectangulo:

    def __init__(self, base, altura):
        
        self.base = base
        self.altura = altura
        
        self.area = self.obtener_superficie()

    def obtener_superficie(self):
        superficie = self.base * self.altura 
        return superficie

    def __str__(self):

        return f"triangulo: {self.base}, {self.altura}. Superficie {self.obtener_superficie()}"

xx = Rectangulo(1, 2) #Crea un objeto de la clase rectangulo y lo guarda en la variable xx
yy = Rectangulo(14, 78)

print(xx)  # Imprime la información del primer rectángulo
print(yy)  # Imprime la información del segundo rectángulo
print(xx.obtener_superficie())  # Imprime el área del primer rectángulo
print(yy.area)  # Imprime el área del segundo rectángulo