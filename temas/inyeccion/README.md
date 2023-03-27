# Inyección

## Definición

La inyección de dependencias es un principio de diseño que permite a una clase tener sus dependencias proporcionadas por una fuente externa en lugar de crearlas internamente. Esto permite una mayor flexibilidad y facilidad de mantenimiento al permitir que las dependencias se intercambien fácilmente sin modificar el código de la clase.

## Inyección en Python

En Python, la inyección de dependencias se puede lograr utilizando la biblioteca `injector`. El siguiente ejemplo muestra cómo se puede implementar la inyección de dependencias en una clase `Motor` que tiene una dependencia `ComponenteMotor`:

#### `motor.py`

```python
import injector

class ComponenteMotor:
    def operar(self):
        pass

class Combustible(ComponenteMotor):
    def operar(self):
        print("El motor está funcionando con combustible.")

class Aceite(ComponenteMotor):
    def operar(self):
        print("El motor está funcionando con aceite.")

class Motor:
    @injector.inject
    def __init__(self, componente: ComponenteMotor):
        self.componente = componente

    def operar(self):
        print("El motor está en marcha.")
        self.componente.operar()

def configurar_inyector(binder, seleccion):
    if seleccion == "combustible":
        binder.bind(ComponenteMotor, to=Combustible)
    elif seleccion == "aceite":
        binder.bind(ComponenteMotor, to=Aceite)
    else:
        raise ValueError("Selección inválida")

if __name__ == "__main__":
    seleccion = input("¿Desea utilizar combustible o aceite? ")
    inyector = injector.Injector(lambda binder: configurar_inyector(binder, seleccion))
    motor = inyector.get(Motor)
    motor.operar()
    seleccion = input("¿Desea utilizar combustible o aceite? ")
    inyector = injector.Injector(lambda binder: configurar_inyector(binder, seleccion))
    motor = inyector.get(Motor)
    motor.operar()
```

En este ejemplo, la clase `Motor` tiene un constructor que toma una dependencia `ComponenteMotor`. En lugar de crear la instancia de `ComponenteMotor` dentro de la clase `Motor`, se utiliza la biblioteca `injector` para proporcionar la dependencia a través de la inyección de dependencias.

El método `configurar_inyector` define cómo se deben vincular las dependencias. En este caso, se vincula la clase `Combustible` o la clase `Aceite` a la clase `ComponenteMotor` en función de la selección del usuario.

El programa principal pide al usuario que seleccione si desea utilizar combustible o aceite para el motor y crea una instancia de la clase `Motor` utilizando la inyección de dependencias para proporcionar la dependencia `ComponenteMotor`. Luego, el programa repite este proceso una vez más para permitir al usuario cambiar la selección de la dependencia y crear una nueva instancia de la clase `Motor` con la dependencia actualizada.

## Conclusiones

La inyección de dependencias es útil para crear clases que sean flexibles y fáciles de mantener al permitir que las dependencias se intercambien fácilmente. En Python, se puede lograr la inyección de dependencias utilizando la biblioteca injector, aunque también se puede lograr utilizando otras bibliotecas como `dependency-injector`.

## Instrucciones de ejecución

Para ejecutar el código anterior, instale el paquete `injector` con el siguiente comando:

```bash
py -m pip install injector
```

Luego, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py motor.py
```