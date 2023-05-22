# Undefined

## Definición

Undefined es un valor que se le puede asignar a una variable cuando no ha sido inicializada. Se recomienda usarlo por encima de `null` para evitar errores.

## Undefined en Python

En Python, no existe el concepto de `undefined`. Sin embargo, se puede simular usando `None`. También existe `Optional`, que es un tipo de dato que puede ser `None` o un valor de otro tipo. En el siguiente ejemplo, se muestra cómo simular `undefined` usando `None` y `Optional`:

#### `stream.py`
```python
from typing import Optional

def get_next_value(stream) -> Optional[int]:
    # Simulación de lectura de un stream
    # Devuelve None si no hay más valores en el stream
    if stream:
        return stream.pop(0)
    else:
        return None

# Procesa un stream de valores. Si el valor es None, se ignorará. Cuando no haya más valores, se terminará la ejecución
def process_stream(stream):
    while True:
        value = get_next_value(stream)
        if value is not None:
            # Realizar algún procesamiento con el valor
            print(value * 2)
        else:
            # No hay más valores en el stream
            if not stream:
                break
        
# Ejemplo de uso
my_stream = [1, 2, 3, None, 4, 5, None, 6, 7]
process_stream(my_stream)
```

En este ejemplo se simula un stream de datos que se lee de forma secuencial. El stream puede contener valores de tipo `int` o `None`. La función `process_stream` lee el stream y realiza algún procesamiento con cada valor. Si se alcanza el final del stream, se termina la ejecución. Si se encuentra un valor `None`, se ignora y se continúa con el siguiente valor.

## Conclusiones

El uso de `undefined` es muy útil, ya que permite diferenciar entre una variable que no ha sido inicializada y una variable que no tiene valor. La mayoría de lenguajes de programación cuentan con este concepto, aunque con diferentes nombres. En Python, se puede simular usando `None`.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py stream.py
```