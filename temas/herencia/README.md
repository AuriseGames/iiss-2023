# Herencia

## Definición

La herencia es un concepto de la programación orientada a objetos que permite la creación de una clase nueva basada en una clase existente. La clase nueva hereda los atributos y métodos de la clase existente y puede añadir nuevos atributos y métodos propios.

La herencia es útil para evitar la duplicación de código y para crear jerarquías de clases que representen una relación "es un" entre las clases.

## Herencia en Python

La herencia en Python se puede lograr utilizando la palabra clave class seguida del nombre de la clase nueva y el nombre de la clase existente entre paréntesis.

Aquí hay un ejemplo de cómo se podría implementar la herencia en Python:

#### `vehiculo.py`

```python
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
```

En este ejemplo, la clase `Coche` hereda los atributos y métodos de la clase `Vehiculo` mediante la línea `class Coche(Vehiculo):`. Además, añade su propio atributo `velocidad_maxima` y el método `get_velocidad_maxima()`.

La función `super().__init__(marca, modelo)` llama al constructor de la clase base `Vehiculo` y establece los valores de `marca` y `modelo`.

Cuando se crea un objeto `Coche`, se pueden llamar a los métodos `get_marca()`, `get_modelo()` y `get_velocidad_maxima()` para obtener los valores de los atributos correspondientes.

## Conclusiones

En conclusión, en este ejemplo se cumple el principio LSP, ya que los objetos de la clase `Coche` pueden ser utilizados en lugar de objetos de la clase `Vehiculo` sin cambiar el comportamiento del programa. Además, se añade una funcionalidad adicional a la clase `Coche` a través del atributo `velocidad_maxima` y el método `get_velocidad_maxima()`, lo cual no afecta al comportamiento de la clase base `Vehiculo`.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py vehiculo.py
```