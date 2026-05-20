import json
with open("Texto.txt","w") as f:
    f.write("Python")

with open("Texto.txt", "w") as f:
    f.write("Python")


with open("Texto.txt", "r") as f:
    contenido = f.read()
    print(contenido)

asd={"x": 10, "y": 20} 
with open("primer.json","w") as f:
    json.dump(asd, f, indent=4)

with open("primer.json","r") as f:
    nombre=json.load(f)
    print(nombre["x"])
usuarios = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 30}
]

with open("primer.json","w") as f:
    json.dump(usuarios,f,indent=4)

with open("primer.json","r") as f:
    resultado=json.load(f)
    for u in resultado:
        print(u["nombre"])

