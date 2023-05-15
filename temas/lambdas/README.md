# Lambdas

## Definición

Las lambdas (también conocidas como funciones anónimas) son funciones pequeñas y anónimas que pueden ser creadas y usadas en línea dentro de otras funciones. Son útiles cuando se necesitan realizar tareas sencillas y se desea hacerlo de forma rápida y sin tener que definir una función completa.

Las lambdas se utilizan comúnmente en la programación funcional, especialmente en lenguajes como Python, JavaScript y Ruby.

## Lambdas en Python

En Python, la sintaxis para definir una lambda es la siguiente:

```python
lambda argumentos : expresion
```

Donde `argumentos` son los argumentos de la función y `expresion` es el código que se ejecuta dentro de la lambda.

#### `multiplica.py`

```python
# Definición de una lista de números
numeros = [1, 2, 3, 4, 5]

# Uso de lambda para multiplicar cada número de la lista por 2
resultado = map(lambda x: x * 2, numeros)

# Impresión del resultado
print(list(resultado)) # Output: [2, 4, 6, 8, 10]
```
En este ejemplo, se define una lista de números y se utiliza la función `map()` para aplicar una lambda que multiplica cada número de la lista por 2. La función `map()` toma dos argumentos: la función a aplicar y la lista (o iterable) sobre la cual se aplicará la función. La lambda en este caso es `lambda x: x * 2`.

## Conclusiones

Las lambdas son una herramienta útil para la programación funcional en Python, ya que permiten crear funciones pequeñas y anónimas de forma rápida y sencilla. Se utilizan comúnmente en funciones como `map()`, `filter()` y `reduce()` para aplicar una función sobre cada elemento de una lista o iterable.

Es importante tener en cuenta que las lambdas tienen ciertas limitaciones, como no poder contener declaraciones condicionales o bucles, lo que puede limitar su capacidad para realizar tareas más complejas. En estos casos, es recomendable utilizar funciones definidas de manera convencional.

## Instrucciones de ejecución

Para ejecutar el código anterior, sitúese en la carpeta python y ejecute el siguiente comando:

```bash
py multiplica.py
```