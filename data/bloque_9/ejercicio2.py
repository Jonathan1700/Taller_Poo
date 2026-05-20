class SistemaGps:
    @staticmethod
    def intentar_modificar():
        try:
            tupla =  (10.5, 20.3, 30.1, 40.7)
            tupla[0] = 10
        except TypeError:
           print ("No se puede modificar")

    @staticmethod
    def desempaquetar_rutas():
        rutas = ("Guayaquil", "Durán", "Milagro", "Naranjal", "Cuenca")
        a, *b, c = rutas
        print (f"Primera ruta: {a}, punto: {b}, resto: {c}")

    @staticmethod
    def recorrer_puntos():
        puntos = [(0,0), (1,5), (3,2), (7,8), (4,6)]

        for x, y in puntos:
            print (f"X = {x}, Y = {y}")

    @staticmethod
    def convertir_y_modificar():
        lista = (10, 20, 30, 40, 50)
        listan = list(lista)
        listan.append(99)
        listan.pop(4)
        nueva_tupla = tuple(listan)         
        print (lista, listan, nueva_tupla)


SistemaGps.intentar_modificar()
SistemaGps.desempaquetar_rutas()
SistemaGps.recorrer_puntos()
SistemaGps.convertir_y_modificar()