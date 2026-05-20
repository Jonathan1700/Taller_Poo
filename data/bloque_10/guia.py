persona = {"nombre": "Juan", "edad": 25}

persona["nombre"]           # → "Juan"
persona.get("telefono", "No existe")  # → acceso seguro sin error

persona["edad"] = 26        # modificar
persona["telefono"] = "099" # agregar
del persona["telefono"]     # eliminar
persona.pop("edad")         # eliminar y retornar


persona.keys()    # claves
persona.values()  # valores
persona.items()   # tuplas (clave, valor)
persona.update({"apellido": "Pérez"})  # combinar
persona.copy()    # copia superficial

cuadrados = {x: x**2 for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}



universidad = {
    "estudiante": {"nombre": "María", "edad": 20},
    "profesor":   {"nombre": "Carlos", "materia": "POO"},
}
print(universidad["estudiante"]["nombre"])  # María