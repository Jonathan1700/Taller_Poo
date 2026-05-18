a, b, c = (1, 2, 3)

# Con * para capturar el resto
primero, *resto, ultimo = (1, 2, 3, 4, 5)
# primero=1, resto=[2,3,4], ultimo=5

# En bucles
coordenadas = [(1,2), (3,4)]
for x, y in coordenadas:
    print(f"x={x}, y={y}")


tupla = (1, 2, 2, 3, 2)
tupla.count(2)   # 3 → cuántas veces aparece
tupla.index(3)  
lista_temp = list(tupla)
lista_temp.append(6)
nueva_tupla = tuple(lista_temp)