numeros = {1, 2, 2, 3, 3 }
print(numeros)  

lista = [1, 2, 2, 3, 3, 3]
s = set(lista)
print(s)  # {1, 2, 3}


# Unión               |   ó   .union() 
# Intersección        &   ó   .intersection() 
# Diferencia          -   ó   .difference() 
# Dif. simétrica      ^   ó   .symmetric_difference() 


# add(x)      → agregar elemento 
#   remove(x)   → eliminar; lanza KeyError si no existe 
#   discard(x)  → eliminar; sin error si no existe 
#   pop()       → eliminar y retornar aleatorio 
#   issubset()  / issuperset()  / isdisjoint()



A = {1, 2, 3, 4} 
B = {3, 4, 5, 6} 
print(A | B)   # {1,2,3,4,5,6} 
print(A & B)   # {3,4} 
print(A - B)   # {1,2} 
print(A ^ B)   # {1,2,5,6} 

print((A | B) - (A & B) )   # {1,2,3,4,5,6} 

   
lista = [1, 2, 2, 3, 3, 3] 
sin_dup = list(set(lista))   # [1, 2, 3]