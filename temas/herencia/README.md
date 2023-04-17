# Herencia

## Definición

La herencia es un concepto de la programación orientada a objetos que permite la creación de una clase nueva basada en una clase existente. La clase nueva hereda los atributos y métodos de la clase existente y puede añadir nuevos atributos y métodos propios.

La herencia es útil para evitar la duplicación de código y para crear jerarquías de clases que representen una relación "es un" entre las clases, aunque el uso de la herencia para crear jerarquías de clases es una mala práctica. En este ejemplo veremos cómo se puede utilizar la herencia para implementar interfaces.

## Herencia en Python

La herencia en Python se puede lograr utilizando la palabra clave class seguida del nombre de la clase nueva y el nombre de la clase existente entre paréntesis.

Aquí hay un ejemplo de cómo se podría implementar la herencia en Python:

#### `animal.py`

```python
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
```

En este código, tenemos tres clases que actúan de interfaces: `Hace_Sonido`, `Come` y `Bola_De_Pelo`. Estas interfaces definen los métodos que deben implementar las clases que hereden de ellas.

La clase `Gato` hereda de las tres interfaces y, por lo tanto, debe implementar los métodos `hacer_sonido`, `comer` y `expulsar_pelo`. La clase `Perro` hereda de las interfaces `Hace_Sonido` y `Come` y, por lo tanto, debe implementar los métodos `hacer_sonido` y `comer`.

La función `observar_animal` recibe un objeto `animal` y comprueba si `animal` implementa la interfaz `Hace_Sonido`, `Come` o `Bola_De_Pelo`. Si `animal` implementa la interfaz, se invoca al método correspondiente. Si no implementa la interfaz, se muestra un mensaje por pantalla.

## Conclusiones

Este es un ejemplo de buen uso de la herencia, ya que se no se utiliza para estructurar el código en jerarquías de clases, sino para definir interfaces que deben implementar las clases que hereden de ellas.

Este código se podría mejorar, ya que si añadimos nuevas funcionalidades a las clases `Gato` y `Perro`, tendremos que modificar la función `observar_animal` para que compruebe si `animal` implementa dichas funcionalidades.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py animal.py
```