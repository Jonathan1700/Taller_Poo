class Diccionarios:
    @staticmethod
    def eje1():
        persona = {"nombre": "Jonathan", "edad": "20", "ciudad": "Milagro"}
        print(persona.get("nombre"))
        print(persona ["nombre"])
    @staticmethod
    def eje2():
        persona = {"nombre": "Jonathan", "edad": "20", "ciudad": "Milagro"}
        for clave, valor in persona.items():
            print (f"{clave}, {valor}")

    @staticmethod
    def eje3():
        dic = {x: x**2 for x in range(5)}
        referencia = dic
        copia_real = dic.copy()
        dic ["nuevo"] = 000


        print(f"Original:   {dic}")
        print(f"Referencia: {referencia}")  
        print(f"Copia real: {copia_real}") 

    

Diccionarios.eje1()
Diccionarios.eje2()
Diccionarios.eje3()



