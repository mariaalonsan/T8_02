"""
resultado = "2" + 10
"""
try:
    resultado = "2" + 10
except TypeError:
    print("Error: No se puede sumar un string y un número directamente.")
    print("Solución: Convierte el string a un número o viceversa antes de sumar.")
