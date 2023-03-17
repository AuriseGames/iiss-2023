# Encapsulación

## Definición

La encapsulación es un concepto de la programación orientada a objetos que se utiliza para ocultar los detalles de implementación de un objeto. Los detalles de implementación incluyen los atributos y métodos de un objeto. 

La encapsulación se logra mediante la restricción del acceso a los atributos y métodos de un objeto.

Los atributos y métodos privados solo se pueden acceder desde dentro del objeto. Los atributos y métodos públicos se pueden acceder desde cualquier parte del código.

## Encapsulación en Python

La encapsulación en Python se puede lograr utilizando los mecanismos del lenguaje, como los métodos y atributos privados y públicos.

Aquí hay un ejemplo de cómo se podría implementar la encapsulación en Python:

#### `persona.py`

```python
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
```

En este ejemplo, el atributo nombre se declara como privado con el doble guion bajo (`__nombre`) y se accede a él a través de los métodos `get_nombre()` y `set_nombre()`. El atributo edad es público y se puede acceder directamente.

Cuando se intenta acceder al atributo privado `__nombre` directamente, se produce un error de `AttributeError`. Esto demuestra que la encapsulación se está aplicando correctamente en el código.

## Conclusiones

En conclusión, en este ejemplo se cumple el principio de encapsulación, ya que los atributos y métodos privados solo se pueden acceder desde dentro del objeto. Esto permite ocultar los detalles de implementación de un objeto y reducir el acoplamiento entre los objetos, lo que cumple con el objetivo de la encapsulación como patrón de diseño.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py persona.py
```