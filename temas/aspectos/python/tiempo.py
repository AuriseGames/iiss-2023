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
