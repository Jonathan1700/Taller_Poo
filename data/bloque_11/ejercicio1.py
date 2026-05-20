class Conjuntos:

    @staticmethod
    def eje1():
        A = {1, 2, 3, 4} 
        B = {3, 4, 5, 6} 
        print (A | B)
        print (A & B)
        print(A - B)

    @staticmethod
    def eje2():
        lista =  [1,2,2,3,3,3,4] 
        n = set(lista)
        print (n)

    @staticmethod
    def eje3():
        A = {1, 2, 3, 4} 
        B = {3, 4, 5, 6} 

        print ((A|B) - (A & B)) # Lo que hace es llamar a todo lo que haya en los conjuntos, quitando lo que este repetido en medio
        
Conjuntos.eje1()
Conjuntos.eje2()
Conjuntos.eje3()