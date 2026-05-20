class Tuplas:
    @staticmethod
    def eje1():
        try:
            tupla = (1,2,3,4)
            tupla[0] = 99
        except TypeError:
            print ("no se puede modificar una tupla")
    @staticmethod
    def eje2():
        a, *b, c = (12,10,5,10,5)
        print(a, *b, c)

    @staticmethod
    def eje3():
        lista = [(10,4), (11,10)]
        for x,y in lista:
            print(f"X = {x}, y = {y}")

Tuplas.eje1()
Tuplas.eje2()
Tuplas.eje3()