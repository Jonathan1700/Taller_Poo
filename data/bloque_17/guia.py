class ValidacionMixin:
    """No se instancia sola — agrega validaciones"""
    
    def validar_nombre(self, nombre):
        if not nombre:
            raise ValueError("Nombre vacío")
    
    def validar_edad(self, edad):
        if edad < 0:
            raise ValueError("Edad inválida")

class SistemaEstudiantes(ValidacionMixin):  # hereda el Mixin
    def __init__(self):
        self.estudiantes = []
    
    def registrar(self, nombre, edad):
        self.validar_nombre(nombre)   # método del Mixin
        self.validar_edad(edad)       # método del Mixin
        self.estudiantes.append({"nombre": nombre, "edad": edad})

sistema = SistemaEstudiantes()
sistema.registrar("Daniel", 20)   # ✅
sistema.registrar("", 20)         # ❌ ValueError: Nombre vacío

class A:
    def metodo(self): print("A")

class B:
    def metodo(self): print("B")

class C(A, B):  # hereda de A primero
    pass

C().metodo()  # imprime "A" — Python usa MRO de izquierda a derecha