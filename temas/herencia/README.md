# Herencia

## Definición

La herencia es un concepto de la programación orientada a objetos que permite la creación de una clase nueva basada en una clase existente. La clase nueva hereda los atributos y métodos de la clase existente y puede añadir nuevos atributos y métodos propios.

La herencia es útil para evitar la duplicación de código y para crear jerarquías de clases que representen una relación "es un" entre las clases.

## Herencia en Python

La herencia en Python se puede lograr utilizando la palabra clave class seguida del nombre de la clase nueva y el nombre de la clase existente entre paréntesis.

Aquí hay un ejemplo de cómo se podría implementar la herencia en Python:

#### `animal.py`

```python
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
```

Este código define una clase base `Animal` con un método `hacer_sonido` que no hace nada. Las clases `Perro` y `Gato` heredan de `Animal` y sobrescriben el método `hacer_sonido` para devolver el sonido que hace cada animal.


## Conclusiones

La función `escuchar_animal` toma un objeto de tipo `Animal` (o una subclase de `Animal`) y lo usa para imprimir el sonido que hace. Como las clases `Perro` y `Gato` son subclases de `Animal`, podemos pasar objetos de tipo `Perro` o `Gato` a la función `escuchar_animal` y el código seguirá funcionando correctamente. Esto demuestra que el código respeta el principio de sustitución de Liskov (LSP).


## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py animal.py
```