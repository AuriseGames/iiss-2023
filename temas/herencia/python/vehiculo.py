class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

coche = Coche("Ford", "Mustang", 250)
print(coche.get_marca())  # Output: "Ford"
print(coche.get_modelo())  # Output: "Mustang"
print(coche.get_velocidad_maxima())  # Output: 250
