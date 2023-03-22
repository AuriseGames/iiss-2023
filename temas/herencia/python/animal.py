class Animal:
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


def escuchar_animal(animal):
    print(animal.hacer_sonido())


perro = Perro()
escuchar_animal(perro)

gato = Gato()
escuchar_animal(gato)