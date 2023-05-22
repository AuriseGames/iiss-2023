# Undefined

## Definición

Undefined es un valor que se le puede asignar a una variable cuando no ha sido inicializada. Se recomienda usarlo por encima de `null` para evitar errores.

## Undefined en Python

En Python, no existe el concepto de `undefined`. Sin embargo, se puede simular usando `None`. También existe `Optional`, que es un tipo de dato que puede ser `None` o un valor de otro tipo. En el siguiente ejemplo, se muestra cómo simular `undefined` usando `None` y `Optional`:

#### `stream.py`
```python
from typing import Optional


def process_stream(stream):
    for number in stream:
        num = parse_number(number)
        if num is not None:
            print(num)
        else:
            print("ERROR")
            break


def parse_number(number) -> Optional[int]:
    try:
        return int(number)
    except ValueError:
        return None


# Ejemplo de uso
stream = ['1', '2', '3', 'a', '4', '5']
process_stream(stream)
```

En este ejemplo, se recibe un stream de datos, que deberían ser números. Si se recibe un dato que no es un número, se imprime `ERROR` y se termina el proceso. Si se recibe un número, se imprime el número. La gracia de usar `Optional` es que se puede saber si el número es `None` o no, y así diferenciar entre un número y un error.

## Conclusiones

El uso de `undefined` es muy útil, ya que permite diferenciar entre una variable que no ha sido inicializada y una variable que no tiene valor. La mayoría de lenguajes de programación cuentan con este concepto, aunque con diferentes nombres. En Python, se puede simular usando `None`. Una pega del uso de Optionals es que no sabremos la causa del error al usar varios Optionals uno detrás de otro. Por ejemplo, si se usa un Optional para parsear un número, y luego se usa otro para dividirlo entre 2, si el número es `None`, no sabremos si es porque el número no se pudo parsear, o porque el número era `None` desde un principio.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py stream.py
```