# Aspectos

## Definición

Los aspectos son un concepto asociado a la programación orientada a aspectos (AOP, por sus siglas en inglés). AOP es un paradigma de programación que permite modularizar aspectos o preocupaciones transversales a través de múltiples objetos y componentes de un sistema, separándolos de la lógica principal del programa.

## Aspectos en Python

A continuación se muestra un ejemplo de cómo implementar aspectos en Python utilizando decoradores. 

#### `tiempo.py`

```python
import time
import functools

def medir_tiempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"Tiempo de ejecución de {func.__name__}: {tiempo_ejecucion} segundos")
        return resultado
    return wrapper

@medir_tiempo
def funcion_1():
    print("Ejecutando función 1")
    # Código de la función 1
    time.sleep(2)  # Simulación de trabajo

@medir_tiempo
def funcion_2():
    print("Ejecutando función 2")
    # Código de la función 2
    time.sleep(3)  # Simulación de trabajo

# Llamada a las funciones
funcion_1()
funcion_2()
```

En este ejemplo, se define un decorador `medir_tiempo` que mide el tiempo de ejecución de una función y lo imprime en pantalla. Este decorador se aplica a las funciones `funcion_1` y `funcion_2`, las cuales se encargan de imprimir un mensaje y simular trabajo.

El decorador `medir_tiempo` recibe como parámetro una función `func` y retorna una función `wrapper` que mide el tiempo de ejecución de `func` y lo imprime en pantalla. Para medir el tiempo de ejecución de `func`, se utiliza la función `time.time` de la librería `time`.

La función `wrapper` recibe como parámetros los argumentos posicionales `*args` y los argumentos nombrados `**kwargs` de `func`. Estos parámetros se utilizan para llamar a `func` y obtener su resultado. Para llamar a `func`, se utiliza la sintaxis `func(*args, **kwargs)`. Finalmente, la función `wrapper` retorna el resultado de `func`.

De esta forma, la lógica principal del programa se encuentra en las funciones `funcion_1` y `funcion_2`, mientras que la preocupación transversal de medir el tiempo de ejecución se encuentra en el decorador `medir_tiempo`.

## Conclusiones

La ventaja de utilizar aspectos es que permite separar las preocupaciones transversales de la lógica principal del programa, lo cual puede facilitar la comprensión, mantenibilidad y reutilización del código. Además, al utilizar aspectos, se evita la repetición de código relacionado con estas preocupaciones en diferentes partes del sistema, promoviendo así la modularidad y la reutilización.

## Instrucciones de ejecución


Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py tiempo.py
```