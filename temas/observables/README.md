# Observables

## Definición

Se refieren a una técnica de programación reactiva que permite la emisión y la suscripción a eventos o cambios en los datos. Los observables son una parte fundamental de la programación reactiva y se utilizan para crear flujos de datos que pueden ser consumidos por otros componentes de forma asíncrona.

## Observables en Python

Un observable en Python es una secuencia de valores que se emiten a lo largo del tiempo. Estos valores pueden ser cualquier tipo de dato, como números, cadenas, objetos, etc. Los observables tienen la capacidad de notificar a los componentes suscritos cada vez que se produce un cambio o un nuevo valor es emitido.

Para el siguiente ejemplo, se utilizará la librería rx de Python, que es una implementación de ReactiveX en Python.

#### `parimpar.py`

```python
from rx import create

# Definir una función que emite números pares
def emitir_numeros_pares(observer, scheduler):
    try:
        for i in range(0, 10, 2):
            observer.on_next(i)
        observer.on_completed()

    except Exception as e:
        observer.on_error(e)

# Definir una función que emite números impares
def emitir_numeros_impares(observer, scheduler):
    try:
        for i in range(1, 10, 2):
            observer.on_next(i)
        # Simular un error lanzando una excepción
        raise ValueError("Error simulado")

    except Exception as e:
        observer.on_error(e)

# Crear un observable a partir de la función
observable1 = create(emitir_numeros_pares)
observable2 = create(emitir_numeros_impares)

# Definir los métodos de suscripción al observable
def on_next(valor):
    print(f'Se recibió el valor: {valor}')

def on_completed():
    print('Se completó la emisión de números pares')

def on_error(error):
    print(f'Se produjo un error: {error}')

# Suscribirse al observable
observable1.subscribe(on_next, on_error, on_completed)
observable2.subscribe(on_next, on_error, on_completed)
```

En este ejemplo creamos dos observables (`observable1` y `observable2`) a partir de dos funciones que emiten números pares e impares respectivamente. Luego, nos suscribimos a cada observable para recibir los valores emitidos. En este caso, los valores emitidos son números enteros, pero podrían ser cualquier tipo de dato, como cadenas, objetos, etc.

La salida del programa es la siguiente:

```bash
Se recibió el valor: 0
Se recibió el valor: 2
Se recibió el valor: 4
Se recibió el valor: 6
Se recibió el valor: 8
Se completó la emisión de números pares
Se recibió el valor: 1
Se recibió el valor: 3
Se recibió el valor: 5
Se recibió el valor: 7
Se recibió el valor: 9
Se produjo un error: Error simulado
```

Las funciones `on_next`, `on_completed` y `on_error` son los métodos de suscripción al observable. El método `on_next` se ejecuta cada vez que se emite un nuevo valor, el método `on_completed` se ejecuta cuando se completa la emisión de valores y el método `on_error` se ejecuta cuando se produce un error.

Las dos ultimas funciones son excluyentes entre sí, es decir, si se ejecuta el método `on_completed`, no se ejecuta el método `on_error` y viceversa. Por lo tanto, si se produce un error, el método `on_completed` no se ejecuta.

## Conclusiones

En resumen, los observables en Python son una herramienta útil para trabajar con flujos de datos asíncronos y reactivos. Permiten la emisión y la suscripción a eventos o cambios en los datos, lo que facilita la programación de aplicaciones que responden de manera eficiente a los eventos y cambios en tiempo real.

## Instrucciones de ejecución

Para ejecutar el ejemplo, es necesario instalar la biblioteca rx de Python:

```bash
pip install rx
```

Una vez instalada, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py parimpar.py
```