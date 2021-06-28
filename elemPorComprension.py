mi_lista = [x**2 for x in range(4, 31, 2) if x%3 == 0]
print(mi_lista)

mi_diccionario = { (y, y**3) : [x**2 for x in range(4, 31, 2) if x%y == 0] for y in range(3, 11) }
print(mi_diccionario)