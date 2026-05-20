class Unpacking:
    @staticmethod
    def eje1():
        primero, * resto, ultimo = (10, 20, 30, 40)
        print(f"Primera: {primero}, Resto: {resto}, Ultimo: {ultimo}")

    def multiplicar(a,b,c):
        return (a * b * c )
    l = [2,3,4]
    print (multiplicar(*l))
    
    @staticmethod
    def eje4():
        d1 = {"a": 1, "b": 2}
        d2 = {"c": 3, "d": 4}
        combinado = {**d1 **d2}
        print (combinado)


    
Unpacking.eje1()
Unpacking.eje4()

        

