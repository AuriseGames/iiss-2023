# Undefined

## Definición

Undefined es un valor que se le puede asignar a una variable cuando no ha sido inicializada. Se recomienda usarlo por encima de `null` para evitar errores.

## Undefined en Python

En Python, no existe el concepto de `undefined`. Sin embargo, se puede simular usando `None`.

#### `informacion.py`

```python
# Funcion que devuelve la informacion de una persona o None si no se encuentra
def obtener_informacion_persona(nombre):
    if nombre == "Juan":
        return {
            "nombre": "Juan",
            "edad": 25,
            "ocupacion": "Estudiante"
        }
    else:
        return None

# Solicita el nombre de una persona
nombre_persona = input("Ingresa un nombre: ")
informacion = obtener_informacion_persona(nombre_persona)

# Comprueba si la información es None
if informacion is None:
    print("No se encontró información para la persona", nombre_persona)
else:
    print("Información de", informacion["nombre"])
    print("Edad:", informacion["edad"])
    print("Ocupación:", informacion["ocupacion"])
```

En este ejemplo, se simula el concepto de `undefined` usando `None`. La función `obtener_informacion_persona` devuelve `None` si no se encuentra información para el nombre de la persona. En caso contrario, devuelve un diccionario con la información de la persona.

## Conclusiones

El uso de `undefined` es muy útil, ya que permite diferenciar entre una variable que no ha sido inicializada y una variable que no tiene valor. La mayoría de lenguajes de programación cuentan con este concepto, aunque con diferentes nombres. En Python, se puede simular usando `None`.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py informacion.py
```