a, b = [1, 2]
a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3


primero, resto, ultimo = [1, 2, 3, 4, 5]
print(primero)  # 1
print(resto)    # [2, 3, 4]
print(ultimo)   # 5

#también funciona así
a, b,resto = (10, 20, 30, 40)
print(a)      # 10
print(b)      # 20
print(resto)  # [30, 40]

def suma(a, b, c):
    return a + b + c

numeros = [1, 2, 3]
print(suma(*numeros))   # equivale a suma(1, 2, 3) → 6

#con diccionarios
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

datos = {"nombre": "Elian", "edad": 22}
presentar(datos)  # equivale a presentar(nombre="Elian", edad=22)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combinado = {**dict1,** dict2}
print(combinado)  # {"a":1, "b":2, "c":3, "d":4}

coordenadas = [(1, 2), (3, 4), (5, 6)]
for x, y in coordenadas:
    print(f"x={x}, y={y}")
