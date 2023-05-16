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
