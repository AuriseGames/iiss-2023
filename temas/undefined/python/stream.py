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