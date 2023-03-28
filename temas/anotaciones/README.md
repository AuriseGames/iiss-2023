# Anotaciones

## Definición

Las anotaciones son metadatos que se añaden a elementos de un programa para proporcionar información adicional sobre su comportamiento o características. Se usan comúnmente en la programación orientada a objetos y en la inyección de dependencias, permitiendo a los frameworks automatizar tareas y personalizar el comportamiento del programa en tiempo de ejecución.

## Anotaciones en Python

En Python, lo que llamamos anotaciones en lenguajes como Java, se denominan decoradores. Los decoradores son funciones que se utilizan para modificar el comportamiento de otras funciones, clases o métodos. En Python, los decoradores se definen utilizando la sintaxis `@` y se aplican a las funciones, clases o métodos que se desean modificar.

#### `motor.py`

```python
class Aceite:
    def operar(self):
        print("El motor está funcionando con aceite.")
        
class Combustible:
    def operar(self):
        print("El motor está funcionando con combustible.")

def usa_aceite(cls):
    cls.dependency = Aceite()
    return cls

def usa_combustible(cls):
    cls.dependency = Combustible()
    return cls

@usa_aceite
class Motor1:
    def operar(self):
        self.dependency.operar()
        
@usa_combustible
class Motor2:
    def operar(self):
        self.dependency.operar()
        
class Motor3:
    def operar(self):
        self.dependency.operar()


motor1 = Motor1()
motor1.operar() # Output: El motor está funcionando con aceite.
motor2 = Motor2()
motor2.operar() # Output: El motor está funcionando con combustible.
motor3 = Motor3()
motor3.operar() # Output: AttributeError: 'Motor3' object has no attribute 'dependency'
```

En este ejemplo, se definen dos decoradores `usa_aceite` y `usa_combustible` que se utilizan para modificar el comportamiento de las clases `Motor1` y `Motor2`. Para crear un decorador, se define una función que recibe como parámetro la clase que se desea modificar. La función debe devolver la clase modificada.

En este caso, la función `usa_aceite` modifica la clase `Motor1` para que su atributo `dependency` sea una instancia de la clase `Aceite`. La función `usa_combustible` modifica la clase `Motor2` para que su atributo `dependency` sea una instancia de la clase `Combustible`.

La clase `Motor3` no tiene ningún decorador, por lo que no tiene el atributo `dependency` y, por lo tanto, no puede ejecutar el método `operar` de su atributo `dependency`.

## Conclusiones

Las anotaciones (decoradores en Python) son muy útiles, ya que permiten modificar el comportamiento de las clases, funciones o métodos sin tener que modificar su código. Esto permite que los frameworks puedan personalizar el comportamiento de las clases, funciones o métodos sin tener que modificar su código.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py motor.py
```