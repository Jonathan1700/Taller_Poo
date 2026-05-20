def mi_decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar")
        resultado = funcion(*args, **kwargs)
        print("Después de ejecutar")
        return resultado
    return wrapper

@mi_decorador
def saludar():
    print("Hola mundo")

saludar()
# Antes de ejecutar
# Hola mundo
# Después de ejecutar

@mi_decorador       # ← equivale a:
def saludar():      # saludar = mi_decorador(saludar)
    pass