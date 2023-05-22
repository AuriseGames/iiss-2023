# Observables

## Definición

Se refieren a una técnica de programación reactiva que permite la emisión y la suscripción a eventos o cambios en los datos. Los observables son una parte fundamental de la programación reactiva y se utilizan para crear flujos de datos que pueden ser consumidos por otros componentes de forma asíncrona.

## Observables en Python

Un observable en Python es una secuencia de valores que se emiten a lo largo del tiempo. Estos valores pueden ser cualquier tipo de dato, como números, cadenas, objetos, etc. Los observables tienen la capacidad de notificar a los componentes suscritos cada vez que se produce un cambio o un nuevo valor es emitido.

Para el siguiente ejemplo, se utilizará la librería rx de Python, que es una implementación de ReactiveX en Python.

#### `observable.py`

```python
import random
import rx
from rx import operators as ops

def filternumbers(x):
   if isinstance(x, int) and x % 2 == 0:
      return x
   else:
      return None

numbers = range(1, 11)
source = rx.from_(numbers)

case1 = source.pipe(
   ops.filter(lambda c: filternumbers(c)),
   ops.map(lambda a: a * 2),
   ops.reduce(lambda acc, curr: acc + curr)
)

case1.subscribe(
   on_next=lambda i: print("Got - {0}".format(i)),
   on_error=lambda e: print("Error: {0}".format(e)),
   on_completed=lambda: print("Job Done!"),
)
```

En el ejemplo anterior, se crea un observable a partir de una lista de números. Luego, se aplica una serie de operadores para filtrar los números pares, multiplicarlos por 2 y sumarlos. Finalmente, se suscribe una función que imprime el resultado de la operación.

## Conclusiones

En resumen, los observables en Python son una herramienta útil para trabajar con flujos de datos asíncronos y reactivos. Permiten la emisión y la suscripción a eventos o cambios en los datos, lo que facilita la programación de aplicaciones que responden de manera eficiente a los eventos y cambios en tiempo real.

## Instrucciones de ejecución

Para ejecutar el ejemplo, es necesario instalar la biblioteca rx de Python:

```bash
pip install rx
```

Una vez instalada, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py observable.py
```