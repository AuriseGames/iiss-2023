# Asincronía

## Definición

La asincronía es un paradigma de programación que permite la ejecución de tareas de forma no bloqueante, lo que significa que las tareas pueden continuar ejecutándose sin tener que esperar a que otras tareas finalicen. Esto se logra mediante el uso de operaciones asíncronas, que permiten a una tarea continuar su ejecución mientras espera la finalización de una tarea de E/S (entrada/salida) o de una tarea que requiere procesamiento.

## Asincronía en Python

En Python, la asincronía se logra mediante el uso de hilos y el módulo `asyncio`. El módulo asyncio proporciona un bucle de eventos que permite la planificación y ejecución de múltiples tareas en un solo proceso.

#### `asincronia.py`

```python
import asyncio

async def descarga_archivo(url, nombre, tamanio):
    print(f"Descargando {url}...")
    await asyncio.sleep(size)  # Simulamos la descarga con una espera de 1 segundo por cada MB
    print(f"Archivo {filename} descargado")

async def main():
    archivos = [
        ("https://ejemplo.com/archivo1.txt", "archivo1.txt", 3),
        ("https://ejemplo.com/archivo2.txt", "archivo2.txt", 2),
        ("https://ejemplo.com/archivo3.txt", "archivo3.txt", 1)
    ]

    hilos = []
    for url, nombre, tamanio in archivos:
        hilo = asyncio.create_task(descarga_archivo(url, nombre, tamanio))
        hilos.append(hilo)

    await asyncio.gather(*hilos)

asyncio.run(main())
```

En este ejemplo, se simula la descarga de tres archivos de diferentes tamaños. Para ello, se crea una función `descarga_archivo` que recibe la URL del archivo, el nombre del archivo y el tamaño del archivo en MB. Esta función imprime un mensaje indicando que se está descargando el archivo, espera un tiempo determinado y luego imprime un mensaje indicando que el archivo se ha descargado.

Para comprobar que los tres hilos se ejecutan al mismo tiempo, se le asigna un mayor tiempo de espera al primer archivo, y un menor tiempo de espera a los otros dos archivos consecutivamente. Si los hilos se ejecutan de forma secuencial, el primer archivo se descargará primero, y luego los otros dos archivos en orden. Sin embargo, si los hilos se ejecutan de forma asíncrona, los tres archivos se descargarán al mismo tiempo, y finaliza primero el archivo que tiene un menor tamaño.


## Conclusiones

La asincronía es muy útil en situaciones en las que se necesitan realizar tareas que pueden tardar un tiempo indeterminado en completarse, como la lectura y escritura de archivos o el acceso a una base de datos remota. En Python, se logra mediante el uso de hilos y el módulo asyncio, lo que permite una ejecución no bloqueante y una gestión eficiente de tareas en un solo proceso.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py asincronia.py
```