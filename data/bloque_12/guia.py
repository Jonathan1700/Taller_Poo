# try:
#     # código que puede fallar
# except TipoError as e:
#     # manejar el error
# else:
#     # se ejecuta si NO hubo error
# finally:
#     # se ejecuta SIEMPRE

# ValueError       # int("abc")
# TypeError        # "hola" + 5
# IndexError       # lista[99]
# KeyError         # dict["noexiste"]
# ZeroDivisionError # 10 / 0
# FileNotFoundError # abrir archivo inexistente


def validar_edad(edad):
    if edad < 0:
        raise ValueError("Edad inválida")
    return edad

# class MiError(Exception):
#     pass

# raise MiError("Error personalizado")

# assert x > 0, "Debe ser positivo"