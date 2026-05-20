class Validaciones:
    @staticmethod
    def registrar(funcion):
        def wrapper (*args , **kwargs): 
            print(f"Ejecutando la funcion: {funcion.__name__}")
            resultado = funcion(*args , **kwargs)
            print(" Completado")
            return resultado
        return wrapper
    
    @staticmethod
    def mayusculas(funcion):
        def wrapper(*args, **kwargs):
            mayuscula = funcion(*args, **kwargs)
            return mayuscula.upper()
        return wrapper

    @staticmethod
    def validar_positivos(funcion):
        def wrapper (*args, **kwargs):
            for x in args:
                if x < 0:
                    raise ValueError ("Deben ser positivos")
            return funcion(*args, **kwargs)
        return wrapper
    
    @staticmethod
    def log_completo(funcion):
        def wrapper(*args, **kwargs):
            print (f" El nombre de la funciones: {funcion.__name__}")
            print (f" Los argumentos recibidos fueron: {args},")
            resultado = funcion(*args, **kwargs)
            return resultado
        return wrapper
    

    @registrar
    @staticmethod
    def saludar(nombre):
        return (f" hola {nombre}")
    
    @mayusculas
    @staticmethod
    def obtener_ciudad():
        return "guayaquil"
    
    @validar_positivos
    @staticmethod
    def multiplicar(a,b):
        return a * b

    @log_completo
    @staticmethod
    def potencia(base, exponente):
        return (base ** exponente)

print(Validaciones.saludar("Julian"))
print("==" *30)
print(Validaciones.obtener_ciudad())
print("==" *30)
print(Validaciones.multiplicar(4,2))
print("==" *30)
print(Validaciones.potencia(5,3))