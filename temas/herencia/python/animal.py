class Hace_Sonido:
    def hacer_sonido(self):
        pass
    
class Come:
    def comer(self):
        pass
        
class Bola_De_Pelo:
    def expulsar_pelo(self):
        pass

class Gato(Hace_Sonido, Come, Bola_De_Pelo):
    def hacer_sonido(self):
        return "Miau"
    def comer(self):
        return "Comiendo pescado"
    def expulsar_pelo(self):
        return "Expulsando pelo"

class Perro(Hace_Sonido, Come):
    def hacer_sonido(self):
        return "Guau"
    def comer(self):
        return "Comiendo carne"


def observar_animal(animal):
    if not isinstance(animal, Hace_Sonido):
        print("No hace sonido")
    else:
        print(animal.hacer_sonido())
        
    if not isinstance(animal, Come):
        print("No come")
    else:
        print(animal.comer())
        
    if not isinstance(animal, Bola_De_Pelo):
        print("No expulsa pelo")
    
    else:
        print(animal.expulsar_pelo())
    

gato = Gato()
observar_animal(gato)

perro = Perro()
observar_animal(perro)