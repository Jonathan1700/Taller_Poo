numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16]

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

from functools import reduce

numeros = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numeros)
# proceso: 1+2=3, 3+3=6, 6+4=10
print(suma)  # 10

numeros = [1, 2, 3, 4, 5, 6]

# cuadrado de los pares
resultado = list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, numeros))
)
print(resultado)  # [4, 16, 36]