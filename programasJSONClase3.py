from funcionesJSONClase3 import *
doc = leer_json("C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/JSON/ej3.json")

#ÍTEM1
print('La lista de provincias son: ')
for prov in listaProvincias(doc):
    print(prov)
print(40*'*')

#ÍTEM2 Muy largo
print('La lista de localidades son: ')
for localidad in listaLocalidades(doc):
    print(localidad)
print(40*'*')

#ÍTEM3
print('La lista de provincias y el total de municipios son: ')
for prov,cant in listaDeProvinciasLocalidades(doc):
    print(prov,cant)
print(40*'*')
