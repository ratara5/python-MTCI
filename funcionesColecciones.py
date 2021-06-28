# 27/05/2021 Funciones sobre Colecciones
# Utilizar la función incorporada map() para crear una función que retorne una lista con la longitud de
# cada palabra (separadas por espacios) de una frase. La función recibe una cadena de texto y retornará
# una lista.

def lonpals(frase):
    fr=frase.split() #Convierte la frase en lista, cada palabra es un elemento
    mapaLon=map(len,fr) #Mapea cada elemento de la lista (fr[i]) y devuelve su longitud (len)
    lon_cad_pala=list(mapaLon) #Convierte en lista el objeto map
    return print("la longitud de cada palabra en la frase "+frase+" es "+str(lon_cad_pala))

ph=(input("por favor introduzca una frase: "))
lonpals(ph)

# Crear una función que tome una lista de dígitos y devuelva al número al que corresponden.
# Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función reduce()

def numero(lista):
    from functools import reduce
    return print(reduce(lambda x,y: x*10+y,lista)) #lambda es una simplificación para una función. reduce es una función
    # ejecutando la operación multiplicar por 10 un elemento y sumarle el siguiente desde el 0esimo hasta completar
    # cada nueva lista, desde la lista inicial.

numero([7,8,9,7,6,5])

#Crear una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Utilizar
#la función filter.

def canpallis(lista,letra):
    return print(list(filter(lambda p: p[0]==letra, lista)))

canpallis(["agua", "abellana", "buho", "casa", "arbol", "sapo"],"s")

# Realizar una función que tome una lista de comprensión para devolver una lista de la misma longitud donde cada valor
# son las dos cadenas de L1 y L2 concatenadas con un conector entre ellas. Ejemplo: Listas: ['A', 'a'] ['B','b']
# Conector: '-' Salida: ['A-a'] ['B-b']. Utilizar la función zip.

def ziplog(lista1, lista2,simbolo):
    op1=([pal1+simbolo+pal2 for pal1, pal2 in (lista1,lista2)])
    op2=([pal1 + simbolo + pal2 for pal1, pal2 in zip(lista1, lista2)])
    return print("Sin usar zip se obtiene "+str(op1)+"\nUsando zip se obtiene "+str(op2))

ziplog(['A','a'],['B','b'],'*')


#lista de valores booleanos donde True corresponde a elemento q es mult3
def equ3(lista):
    igu3=list((map(lambda num: num%3==0, lista)))
    return igu3

print(equ3([x**2 for x in range(0,10)]))

#lista con elementos q son mult3
def equ3(lista):
    igu3=list((filter(lambda num: num%3==0, lista)))
    return igu3

print(equ3([x**2 for x in range(0,10)]))



