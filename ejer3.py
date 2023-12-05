"""
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
paises["alemania"]
"""

try:
    lista = [4, 7, 30, 23, 5]
    print(lista[10])
except IndexError:
    print("Error: Índice fuera del rango de la lista.")
