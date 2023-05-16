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