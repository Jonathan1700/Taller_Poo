from functools import reduce
class ejem2:
    @staticmethod
    def presentar():
        numeros=[2, 4, 6]
        ne=list(map(lambda x:x+1,numeros))
        print(ne)
    @staticmethod
    def filte():
        numeros=[1, 2, 3, 4, 5]
        nea=list(filter(lambda x:x>3,numeros))
        print(nea)

    @staticmethod
    def redu():
        nume=[1, 2, 3, 4]
        new=reduce(lambda x,y:x*y,nume)
        print(new)

ejem2.presentar()
print("="*40)
ejem2.filte()
print("="*40)
ejem2.redu()
print("="*40)
