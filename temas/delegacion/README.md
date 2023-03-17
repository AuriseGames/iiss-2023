# Delegación

## Definición

La delegación es un patrón de diseño que se utiliza en programación orientada a objetos para permitir que un objeto pase ciertas responsabilidades a otro objeto. En lugar de realizar todas las tareas por sí solo, el objeto delega algunas de ellas a otros objetos especializados.

La delegación se utiliza para simplificar la estructura de un objeto y reducir su complejidad, así como para permitir una mayor flexibilidad en la organización y distribución de tareas en un programa.

## Delegación en Python

En Python, la delegación se puede lograr utilizando la composición de objetos. Esto implica crear objetos que contengan otros objetos y delegar ciertas responsabilidades a ellos.

Aquí hay un ejemplo de cómo se podría implementar la delegación en Python:

#### `cliente.py`

```python
class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def pagar(self, monto):
        print(f"{self.nombre} paga {monto}")

class Compra:
    def __init__(self, cliente, monto):
        self.cliente = cliente
        self.monto = monto

    def realizar_pago(self):
        self.cliente.pagar(self.monto)

cliente = Cliente("Juan", "Calle 123")
compra = Compra(cliente, 100)
compra.realizar_pago()  # Output: "Juan paga 100"
```

En este ejemplo, la clase `Compra` contiene una referencia a un objeto `Cliente`, que se le pasa como parámetro en el constructor. El objeto `Compra` delega la responsabilidad de pagar el monto al objeto `Cliente` mediante el método `pagar()`.

El objeto `Compra` puede ser utilizado para realizar pagos para diferentes clientes, lo que permite una mayor flexibilidad en el diseño del programa.

## Conclusiones

En conclusión, en este ejemplo se cumple el principio de delegación, ya que la clase `Compra` delega la responsabilidad de pagar al objeto `Cliente`. Esto permite una mayor flexibilidad en la organización y distribución de tareas en el programa, lo que cumple con el objetivo de la delegación como patrón de diseño.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py cliente.py
```