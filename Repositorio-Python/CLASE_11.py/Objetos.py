class Triangulo:

    def __init__(self, base, altura, lado_extra):
        
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra
        self.area = self.obtener_superficie()

    def obtener_superficie(self):
        superficie = (self.base * self.altura) / 2
        return superficie

    def __str__(self):

        return f"triangulo: {self.base}, {self.altura}, {self.lado_extra}. Superficie {self.obtener_superficie()}"

xx = Triangulo(1, 2, 3)
yy = Triangulo(14, 78, 34)


print(xx.obtener_superficie())
print(yy.area)
