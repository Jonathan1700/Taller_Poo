class SistemaBancario:
    
    @staticmethod
    def depositar():
        try:
            monto = int(input("Ingresa el monto a depositar"))
            if monto < 0:
                raise ValueError (" DEBE SER UN MONTO POSITIVO ")
        except ValueError as e:
            print (f"error: {e}")
        else:
            print (f"el deposito de {monto} fue exitoso")
        finally:
            print ("Operacion finalizada")
        
    @staticmethod
    def retirar():
        try:
            saldo = 0
            monto = int(input("Ingresa el monto a retirar"))
        except ValueError:
            print("Solo ingrese numeros ")
        else:
            if saldo <= 0 or monto > saldo:
                raise ZeroDivisionError ("saldo insuficiente")
        finally:
            print (f"retiraste un monto de {monto}")

    @staticmethod
    def buscar_movimiento():
        try:
            lista = [100, 250, 500, 75, 300]
            indice = int(input("ingrese el indice que desea: "))
            print (f"Movimiento: {lista[indice]}")
        except ValueError:
            print("ingreese un numero")
        except IndexError:
            print ("No hay nada en esa posicion")
        


    
            



            
