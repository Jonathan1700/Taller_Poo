class PromedioMixin:
    def calcular_promedio(self, notas):
        promedio=sum(notas)/len(notas)
        return promedio
        

class Estudiante(PromedioMixin):  
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    
    def mostrar_promedio(self):
        promedio = self.calcular_promedio(self.notas)  
        print(f"{self.nombre} tiene promedio: {promedio}")


estu = Estudiante("Elian", [8, 9, 10])
estu.mostrar_promedio()  

class ValidacionMixin:
    def validar_email(self, correo):
        if "@" not in correo or ".com" not in correo:
            raise ValueError("Email inválido")
    
    def validar_edad(self, edad):
        if edad<18:   
            raise ValueError("Debe ser mayor de edad")

class Usuario(ValidacionMixin):
    def __init__(self, nombre, email, edad):
        self.validar_email(email)   #
        self.validar_edad(edad)     
        self.nombre = nombre
        self.email = email
        self.edad = edad

try:
    u1 = Usuario("Elian", "elian@gmail.com", 22)
    print(f"{u1.nombre} registrado ")
except ValueError as e:
    print(f"Error: {e}")


try:
    u2 = Usuario("Ana", "anacorreo", 20)
except ValueError as e:
    print(f"Error: {e}")  


try:
    u3 = Usuario("Luis", "luis@gmail.com", 15)
except ValueError as e:
    print(f"Error: {e}")

import json

class ExportarMixin:
    def exportar_json(self, datos):
        return json.dumps(datos, indent=2)  
    
    def exportar_csv(self, datos):
 
        return ",".join(str(v) for v in datos.values())  

class Reporte(ExportarMixin):
    def __init__(self, datos):
        self.datos = datos
    
    def mostrar(self):
        print("=== JSON ===")
        print(self.exportar_json(self.datos))    
        print("=== CSV ===")
        print(self.exportar_csv(self.datos))     

reporte = Reporte({"nombre": "Elian", "edad": 22, "carrera": "Sistemas"})
reporte.mostrar()