class SaldoInsuficienteError(Exception):
    pass

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
            monto = int(input("Ingrese el monto a retirar: "))
            if saldo == 0:
                raise ZeroDivisionError ("saldo es cero")
            if monto > saldo:
                raise ValueError ("saldo insuficiente")
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print (e) 
        finally:
            print ("Operacion finalizada")
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


    @staticmethod
    def excepcion_personalizada():
        try:
            saldo = float(input("Tu saldo actual: "))
            monto = float(input("Monto a retirar: "))

            if monto > saldo:
                raise SaldoInsuficienteError("Saldo insuficiente para esta operación")
        
            print(f"Retiro de ${monto} exitoso. Saldo restante: ${saldo - monto:.2f}")
        except SaldoInsuficienteError as e:
            
            print(f" Error: {e}")
        finally:
            print ("proceso finalizado")
 

        


    
            
SistemaBancario.depositar()
SistemaBancario.retirar()
SistemaBancario.buscar_movimiento()
SistemaBancario.excepcion_personalizada()

            
