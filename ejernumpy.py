import numpy as np

# Ejercicio 1 - Crear un vector con valores dentro del rango 10 a 50

a = np.arange(10, 51)

print(a)

# Ejercicio 2 - Invertir el vector

print(a[::-1])

# Ejercicio 3 - Crear una matriz 3x3 con valores de 0 a 8

print(np.arange(0, 9).reshape(3, 3))

# Ejercicio 4 - Encontrar los índices que no son ceros del arreglo [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0

a = np.array([2, 3, 1, 4, 7, 6, 8, 0, 4, 3, 2, 5, 7])
print(np.argwhere(a != 0))

# Ejercicio 5 - Crear una matriz identidad de 6x6

print(np.identity(6))

# Ejercicio 6 - Crear una matriz con valores al azar con forma 3x3x3

r = np.random.random((3, 3, 3))
print(r)

#
# # Ejercicio 7 - Encontrar los índices de los valores mínimos y máximos de la anterior matriz

print(r.argmax())
print(r.ravel()[r.argmax()])

print(np.unravel_index(r.argmax(), r.shape)) # segmento, fila, columna
# print(r[np.unravel_index(r.argmax(), r.shape)])

# Ejercicio 8 Crear una matriz de 10x10 con 1's en los bordes y 0 en el interior (con rangos de índices)

z = np.ones((10, 10))
z[1:-1,1:-1] = 0
print(z)

# Ejercicio 9 - Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4

print(np.tile(np.arange(0, 5), 5).reshape(5, 5))

# Ejercicio 10 - Crear dos arreglos al azar A y B, verificar si son iguales

a = np.random.random((3, 3))
b = np.random.random((2, 2))

print(a == b)
