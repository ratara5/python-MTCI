#funciones
import json
import sys

def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos=json.load(f)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

#Función para saber la cantidad de una fruta o verdura
def cantidadQue(fichero,que):
    if fichero["Fruteria"][1]["Verdura"][0]["Nombre"]==que:
        return fichero["Fruteria"][1]["Verdura"][0]["Cantidad"]
    if fichero["Fruteria"][0]["Fruta"][0]["Nombre"]==que:
        return fichero["Fruteria"][0]["Fruta"][0]["Cantidad"]
    else:
        return(0)

#Función para saber frutas y verduras y sus cantidades
def cantidadFruver(fichero):
    itemFruver=[]
    cantidadesFruver=[]
    for tipo in fichero["Fruteria"]: #fichero(fruteria) es una lista//tipo es un diccionario
        for nombre, cosa in tipo.items(): #cosa es una lista
            for it in cosa: #item es un diccionario
                itemFruver.append(it["Nombre"])
                cantidadesFruver.append(it["Cantidad"])
        # for cosa in tipo:
        #     cosaVerduras.append(cosa["Nombre"])
        #     cantidadFrutas.append(cosa["Cantidad"])
    return list(zip(itemFruver,cantidadesFruver))