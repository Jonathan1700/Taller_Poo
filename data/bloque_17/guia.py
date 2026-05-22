class ValidacionMixin:

    
    def validar_nombre(self, nombre):
        if not nombre:
            raise ValueError("Nombre vacío")
    
    def validar_edad(self, edad):
        if edad < 0:
            raise ValueError("Edad inválida")

class SistemaEstudiantes(ValidacionMixin):  
    def __init__(self):
        self.estudiantes = []
    
    def registrar(self, nombre, edad):
        self.validar_nombre(nombre)   
        self.validar_edad(edad)       
        self.estudiantes.append({"nombre": nombre, "edad": edad})

sistema = SistemaEstudiantes()
sistema.registrar("Daniel", 20)   
sistema.registrar("", 20)         

class A:
    def metodo(self): print("A")

class B:
    def metodo(self): print("B")

class C(A, B): 
    pass

C().metodo()  