# Asincronía

## Definición

La asincronía es un paradigma de programación que permite la ejecución de tareas de forma no bloqueante, lo que significa que las tareas pueden continuar ejecutándose sin tener que esperar a que otras tareas finalicen. Esto se logra mediante el uso de operaciones asíncronas, que permiten a una tarea continuar su ejecución mientras espera la finalización de una tarea de E/S (entrada/salida) o de una tarea que requiere procesamiento.

## Asincronía en Python

En Python, la asincronía se logra mediante el uso de hilos y el módulo `asyncio`. El módulo asyncio proporciona un bucle de eventos que permite la planificación y ejecución de múltiples tareas en un solo proceso.

#### `asincronia.py`

```python
import asyncio

async def foo():
    print('Comenzando foo')
    await asyncio.sleep(1)
    print('Terminando foo')

async def bar():
    print('Comenzando bar')
    await asyncio.sleep(2)
    print('Terminando bar')

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())

    await task1
    await task2

asyncio.run(main())
```

En este ejemplo, se definen dos hilos, `foo` y `bar`. Luego se crea un objeto `task` para cada hilo mediante la función `asyncio.create_task`. Finalmente, se ejecutan ambas tareas mediante la llamada a `await` en la función `main`.


## Conclusiones

La asincronía es muy útil en situaciones en las que se necesitan realizar tareas que pueden tardar un tiempo indeterminado en completarse, como la lectura y escritura de archivos o el acceso a una base de datos remota. En Python, se logra mediante el uso de hilos y el módulo asyncio, lo que permite una ejecución no bloqueante y una gestión eficiente de tareas en un solo proceso.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py asincronia.py
```