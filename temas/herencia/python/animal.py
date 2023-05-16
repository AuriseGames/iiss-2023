import inspect

class Hace_Sonido:
    def hacer_sonido(self):
        pass
    
class Come:
    def comer(self):
        pass
        
class Expulsa_pelo:
    def expulsar_pelo(self):
        pass

class Gato(Hace_Sonido, Come, Expulsa_pelo):
    def hacer_sonido(self):
        print("Miau") 
    def comer(self):
        print("Comiendo pescado")
    def expulsar_pelo(self):
        print("Expulsando pelo")

class Perro(Hace_Sonido, Come):
    def hacer_sonido(self):
        print("Guau")
    def comer(self):
        print("Comiendo carne")


def observar_animal(animal):
    metodos = inspect.getmembers(animal)
    metodos_implementados = [nombre for nombre, _ in metodos if not nombre.startswith("__")]
    for nombre_metodo in metodos_implementados:
        funcion = getattr(animal, nombre_metodo)
        funcion()

    
gato = Gato()
observar_animal(gato)

perro = Perro()
observar_animal(perro)