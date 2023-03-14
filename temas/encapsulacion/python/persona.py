class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.edad = edad        # atributo público

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def cumpleanios(self):
        self.edad += 1

persona = Persona("Juan", 25)
print(persona.get_nombre())  # Output: "Juan"

persona.set_nombre("Pedro")
print(persona.get_nombre())  # Output: "Pedro"

persona.edad = 26
print(persona.edad)  # Output: 26

persona.cumpleanios()
print(persona.edad)  # Output: 27

print(persona.__nombre)  # Error: AttributeError: 'Persona' object has no attribute '__nombre'