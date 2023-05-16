# Lambdas

## Definición

Las lambdas (también conocidas como funciones anónimas) son funciones pequeñas y anónimas que pueden ser creadas y usadas en línea dentro de otras funciones. Son útiles cuando se necesitan realizar tareas sencillas y se desea hacerlo de forma rápida y sin tener que definir una función completa.

Las lambdas se utilizan comúnmente en la programación funcional, especialmente en lenguajes como Python, JavaScript y Ruby.

## Funciones anonimas en Python

En Python, además de las expresiones lambda, existen otras dos formas de crear funciones anónimas: generators expressions y list comprehension. A continuación, se muestra un ejemplo de cada una de ellas.

#### `multiplica.py`

```python
# ---------------------------------------------------------------

# Ejemplo de uso de lambdas en python
numeros = [1, 2, 3, 4, 5]

# Uso de lambda para multiplicar cada número de la lista por 2
resultado = map((lambda x: x * 2), numeros)

# Impresión del resultado
print("\nResultado funcion lambda")
print(resultado) # Output: <map object at 0x[...]>
print(resultado.__next__()) # Output: 2
print(resultado.__next__()) # Output: 4
print(resultado.__next__()) # Output: 6
print(resultado.__next__()) # Output: 8
print(resultado.__next__()) # Output: 10

# ---------------------------------------------------------------

# Ejemplo de generators expressions en python
numeros = [1, 2, 3, 4, 5]

# Uso de generators expressions para multiplicar cada número de la lista por 2
resultado = (x * 2 for x in numeros)

# Impresión del resultado
print("\nResultado generators expressions")
print(resultado)            # Output: <generator object <genexpr> at 0x[...]>
print(resultado.__next__()) # Output: 2
print(resultado.__next__()) # Output: 4
print(resultado.__next__()) # Output: 6
print(resultado.__next__()) # Output: 8
print(resultado.__next__()) # Output: 10
    
# ---------------------------------------------------------------

# Ejemplo de list comprehension en python
numeros = [1, 2, 3, 4, 5]

# Uso de list comprehension para multiplicar cada número de la lista por 2
resultado = [x * 2 for x in numeros]

# Impresión del resultado
print("\nResultado list comprehension")
print(resultado) # Output: [2, 4, 6, 8, 10]

# ---------------------------------------------------------------
```

En el primer ejemplo, se utiliza una lambda para multiplicar cada número de la lista por 2. En el segundo ejemplo, se utiliza una generators expression para realizar la misma tarea. En el tercer ejemplo, se utiliza una list comprehension para realizar la misma tarea.

En el ejemplo de la función lambda, utilizamos `map()` para que se ejecute la función anónima para cada valor de la lista.

La diferencia fundamental entre las lambdas y las generators expressions es que las funciones lambda se ejecutan inmediatamente, mientras que las generators expressions se ejecutan cuando se solicita el siguiente elemento de la secuencia.

Las list comprehensions son similares a las generators expressions, pero en lugar de generar una secuencia, generan una lista. Esto significa que las list comprehensions son menos eficientes que las generators expressions, ya que se almacenan en la memoria.



## Conclusiones

Las lambdas son funciones anónimas que se utilizan para realizar tareas sencillas de forma rápida y sin tener que definir una función completa. En Python, además de las expresiones lambda, existen otras dos formas de crear funciones anónimas: generators expressions y list comprehension. Cada una de estas formas tiene sus propias ventajas y desventajas, por lo que es importante conocerlas para poder elegir la más adecuada para cada caso.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py multiplica.py
```