class decoradores:

    @staticmethod
    def iniciando(funcion):
        def wrapper (*args, **kwargs):
            print ("Antes de ejecutar")
            resultado = funcion(*args, **kwargs)
            print ("despues de ejecutar")
            return resultado
        return wrapper

    @staticmethod
    def verificador(funcion):
        def wrapper (numero):
            if numero < 0:
                return "el numero debe ser positivo"
            return funcion(numero)
        return wrapper
    
    def log(funcion):
        def wrapper(*args, **kwargs):
            print (f"llamando a la funcion: {funcion.__name__}")
            resultado = funcion (*args, **kwargs)
            print (f"Resultado: {resultado}")
            return resultado
        return wrapper
    
    @log
    def suma (a,b):
        return a + b
            # Lo que hace primeramenmte es que en el print del wrapper espera el nombre de la funcion que le vayamos a enviar para poder imprimirla

    @iniciando
    @staticmethod
    def hola():
        print ("te estoy saludando")

    @verificador
    @staticmethod
    def calcular(numero):
        return numero **2



decoradores.hola()
print(decoradores.calcular(6))
print(decoradores.suma(3,5))

