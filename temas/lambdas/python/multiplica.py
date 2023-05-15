# Definición de una lista de números
numeros = [1, 2, 3, 4, 5]

# Uso de lambda para multiplicar cada número de la lista por 2
resultado = map(lambda x: x * 2, numeros)

# Impresión del resultado
print(list(resultado)) # Output: [2, 4, 6, 8, 10]