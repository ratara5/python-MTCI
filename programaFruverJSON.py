from funcionesFruverJSON import *
doc = leer_json("C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/JSON/fruver.json")


#Saber la cantidad de una fruta o verdura
averigua=input(str("De qué fruta o verdura desea saber la cantidad: "))
print("La cantidad de "+averigua+" es: "+str(cantidadQue(doc,averigua)))

#Saber frutas y verduras con sus cantidades
for items, cantidades in cantidadFruver(doc):
    print("Los(as) "+str(items)+"s son: "+str(cantidades))

