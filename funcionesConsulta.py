# 27/05/2021 Funciones de Consulta
# Realizar una función que tome una lista y retorne un diccionario que contenga los valores de la lista
# como clave y el índice como el valor. Utilizar la función enumerate.


def listodic(lista):
    return {key:value for key,value in enumerate(lista)}

list=["Alba","Álvaro","Raymond"]
print(listodic(list)) #imprimir fuera de la definición

# Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo valor es igual a su índice.
# Utilizar la función enumerate.

def caneleguin(lista):
    return len([num for count,num in enumerate(lista) if num==count])


list = [0, 1, 3]
print(caneleguin(list))  # imprimir fuera de la definición

