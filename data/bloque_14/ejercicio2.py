class SistemaEnvios:
    @staticmethod
    def desampaquetar_direccion():
        ruta = ("Ecuador", "Guayaquil", "Milagro", "Naranjal", "Cuenca")
        pais, *ciudades, destino_final = ruta 
        print ( pais, *ciudades, destino_final)


    @staticmethod
    def calcular_costos(*pesos):
        precio = 2.50
        total = 0

        for i, peso in enumerate(pesos, start = 1):
            costo_individual = pesos * precio
            total += costo_individual
            print(f" Envios {i} ({pesos} kg): {costo_individual}.2f")
        print(f"Ciosto total: ${total:.2f}")

    
    @staticmethod
    def combinar_datos():
        cliente = {"nombre": "Jonathan", "ciudad": "Milagro"}
        producto = {"articulo": "Laptop", "precio": 900}
        
        datos_completos = {**cliente, **producto}
        
        print("--- 3. Combinar Datos ---")
        print(f"Diccionario combinado:\n{datos_completos}\n")

    @staticmethod
    def swap():
        a = 10
        b = 20
        print("--- 4. Swap ---")
        print(f"Antes del swap: a = {a}, b = {b}")
        
       
        a, b = b, a
        
        print(f"Después del swap: a = {a}, b = {b}\n")


SistemaEnvios.desempaquetar_direccion()
SistemaEnvios.calcular_costo(1.5, 5.0, 10.2)  
SistemaEnvios.combinar_datos()
SistemaEnvios.swap()
    


      
