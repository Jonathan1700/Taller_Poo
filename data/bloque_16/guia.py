"r"  # lectura — error si no existe
"w"  # escritura — sobrescribe si existe
"a"  # append — agrega al final sin borrar
"x"  # crear — error si ya existe
# escribir
with open("archivo.txt", "w") as f:
    f.write("Hola mundo\n")
    f.write("Segunda línea\n")

# leer todo de una vez
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# leer línea por línea
with open("archivo.txt", "r") as f:
    for linea in f:
        print(linea.strip())  # strip() elimina el \n del final


import json

# guardar
datos = {"nombre": "Juan", "edad": 25, "activo": True}
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=2)  # indent=2 para formato legible

# cargar
with open("datos.json", "r") as f:
    cargado = json.load(f)
    print(cargado["nombre"])  # Juan

# lista de objetos
usuarios = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 30}
]
with open("usuarios.json", "w") as f:
    json.dump(usuarios, f, indent=2)

# cargar y recorrer
with open("usuarios.json", "r") as f:
    data = json.load(f)
    for u in data:
        print(u["nombre"])