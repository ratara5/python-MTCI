from funcionesJSONClase2 import *

doc = leer_json(
    "C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/JSON/pruebas.json")

#pruebas.json: es una lista con objetos json

# •    ¿Cuantas pruebas de idiomas están descritas en el documento?
print('La cantidad de pruebas de idiomas son: %d' % len(doc))
print(40 * '*')

# •    Devuelve el título de las pruebas de nivel que van a durar más de dos horas.
print('Las pruebas que duran más de dos horas son: ')
for titulo in pruebasMasDeDosHoras(doc):
    print(titulo)
print(40 * '*')

#• De las pruebas de tipo “No Presencial” devuelve la URL de información.
print('La URL de las pruebas no presenciales son: ')
for url in urlPruebasNoPresenciales(doc):
    print(url)
print(40*'*')

#• Recibe el código de la prueba “ID” y muestra su título y profesores.
id = input('Dame el id de una prueba: ')
datos = pruebaTitulosProfesores(doc,id)
if len(datos)>0:
    print('El titulo es: ', datos.get('titulo'))
    print('profesores')
    for profesor in datos.get('profesores'):
        print(profesor)
else:
    print('No existe ese id de prueba')

print(40*'*')

#• Para cada uno de las pruebas, muestra su título y sus profesores.
for titulo,profesores in infoPrueba(doc):
    print(titulo)
    print('Profesores: ')
    for profesor in profesores:
        print('\t'+profesor)
print(40*'*')
