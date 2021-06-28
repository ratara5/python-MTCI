# crear dos ficheros: funciones y programa
# FUNCIONES
import json
import sys

def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos = json.load(f)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

# Función que permite saber cuales prubeas duran más de dos horas
def pruebasMasDeDosHoras(doc):
    titulos = []
    for prueba in doc:
        if prueba.get('Horas') > 2:
            titulos.append(prueba.get('Titulo'))
    return titulos

#Función que permite ver las url de las pruebas no presenciales
def urlPruebasNoPresenciales(doc):
    urls = []
    for prueba in doc:
        if prueba.get('TipoFormacion')=="NoPresencial":
            urls.append(prueba.get('URL'))
    return urls

#Función para devolver el título  y lista de profesores creando un diccionario
def pruebaTitulosProfesores(doc,id):
    prueba_econtrada={}
    for prueba in doc:
        if prueba.get('$id')==id:
            prueba_econtrada['titulo']=prueba.get('Titulo')
            prueba_econtrada['profesores']=[]
            for profesor in prueba.get('Profesorado'):
                prueba_econtrada.get('profesores').append(profesor.get('NombreCompleto'))
            return prueba_econtrada
    return prueba_econtrada

#Función para mostrar de cada una de las pruebas su titulo y profesores con dos listas y método zip
def infoPrueba(doc):
    titulos=[]
    profesores=[]
    for prueba in doc:
        titulos.append(prueba.get('Titulo'))
        lista_prof=[]
        for profesor in prueba.get('Profesorado'):
            lista_prof.append(profesor.get('NombreCompleto'))
        profesores.append(lista_prof)
    return zip(titulos,profesores)

