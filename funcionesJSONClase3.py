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

#• Función que devuelve todas las provincias.
def listaProvincias(doc):
    prov=[]
    for provincia in doc['lista']['provincia']:
        prov.append(provincia['nombre']['__cdata'])
    return prov

# •    Función que devuelve todos las localidades.
def listaLocalidades(doc):
    loc = []
    for provincia in doc['lista']['provincia']:
        if type(provincia['localidades']['localidad']) == list:
            for localidad in provincia['localidades']['localidad']:
                loc.append(localidad['__cdata'])
        else:
            loc.append(provincia['localidades']['localidad']['__cdata'])

    return loc

#FUNCION que devuelve provincia y cantidad de localidades usando zip
def listaDeProvinciasLocalidades(doc):
    prov=[]
    cantidades=[]
    for provincia in doc['lista']['provincia']:
        prov.append(provincia['nombre']['__cdata'])
        if type(provincia['localidades']['localidad'])==list:
            cantidades.append(len(provincia['localidades']['localidad']))
        else:
            cantidades.append(1)
    return zip(prov,cantidades)
