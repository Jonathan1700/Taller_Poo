class SistemasCarreras:
    @staticmethod
    def operaciones_basicas():
        informatica = {"Python", "Java", "C++", "SQL", "JavaScript"}
        marketing   = {"SQL", "Excel", "PowerBI", "Python", "Canva"}
        print (informatica | marketing)
        print (informatica & marketing)
        print (informatica - marketing)
    
    @staticmethod
    def elimar_duplicados():
        l = ["Python", "Java", "Python", "SQL", "Java", "C++", "SQL"]
        n = set(l)
        print(n)
        print(l)

    @staticmethod
    def diferencia_simetrica():
        informatica = {"Python", "Java", "C++", "SQL", "JavaScript"}
        marketing   = {"SQL", "Excel", "PowerBI", "Python", "Canva"}
        print (f"{informatica ^ marketing}")

    @staticmethod
    def metodos_set():
        conjunto = {10, 20, 30, 40}
        conjunto.add(50)
        conjunto.discard(20)
        print (f"Conjunto: {conjunto}")
        print (f"¿{{10,30}} es subconjunto? {({10, 30}).issubset(conjunto)}")

SistemasCarreras.operaciones_basicas()
SistemasCarreras.elimar_duplicados()
SistemasCarreras.diferencia_simetrica()
SistemasCarreras.metodos_set()        