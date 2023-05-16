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
