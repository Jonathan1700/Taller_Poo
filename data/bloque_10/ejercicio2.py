class SistemasProductos:
    @staticmethod
    def acceder_productos():
        producto = {"nombre": "lechita", "precio": 1.20, "stock": 10, "categoria": "lactosa"}
        print(producto["precio"])
        producto.get("descuento", "Sin descuento")

    @staticmethod
    def iterar_productos():
        productos = {"laptop": 900, "mouse": 25, "teclado": 45, "monitor": 350}
        print(productos.items())

    @staticmethod
    def comprehension_precios():
        productos = {"laptop": 900, "mouse": 25, "teclado": 45, "monitor": 350}
        decuentos = {nombre: precio * 0.2 for nombre, precio in productos.items()}
        print(f"Original: {productos}")
        print(f"Con descuento:{decuentos}")

    
    @staticmethod
    def referencia_vs_copia():
        producto = {"nombre": "lechita", "precio": 1.20, "stock": 10, "categoria": "lactosa"}
        referencia = producto
        copia_real = producto.copy

        producto["garantia"] = ["2 años"]

        print(producto)
        print(referencia)
        print(copia_real)





SistemasProductos.iterar_productos()  
SistemasProductos.iterar_productos()
SistemasProductos.comprehension_precios()





