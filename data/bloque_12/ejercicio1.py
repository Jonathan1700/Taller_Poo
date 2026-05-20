class Try:
    @staticmethod
    def eje1():
        while True:
            try:
                prueba = int(input("Ingrese un numero: "))
                break
            except ValueError:
                print("Ingresa numeros pe ")
    @staticmethod
    def eje2():
        try:
            lista = [1,2,3]
            print(lista[5])
        except IndexError:
            print ("no esta en el rango")

    @staticmethod
    def eje3():
        try:
            numero = int(input("Ingrese un numero para operar: "))
            resultado = 10 / numero
            print (f"Resultado: {resultado}")
        except ValueError:
            print("Ingrese un numero no una letra")
        except ZeroDivisionError:
            print ("no puedes dividir para 0")
        
Try.eje1()   
Try.eje2()
Try.eje3()