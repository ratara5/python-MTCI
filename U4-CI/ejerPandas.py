# Actividad 1

print ("Actividad 1")
import pandas as pd
#print ("")

#Actividad 2

'''print ("Actividad 2")
datos = [2, 3, 5, 7, 11]
serie = pd.Series(datos)
print(serie)'''

#Convertir un objeto Series a una lista Python.
'''datos = [2,3,5,7,11,15,18,2,3,4]
serie = pd.Series(datos)
print(serie)
lista = serie.tolist()
print(lista)
print("")'''

#Aplicar las operaciones aritméticas básicas sobre objetos Series.

'''serie1 = pd.Series([1,2,3,4,5])
serie2 = pd.Series([9,8,7,6,5])
print(serie1+serie2)
print(serie1-serie2)
print(serie1*serie2)
print(serie1/serie2)
print("")'''
#Usar operadores relacionales para comparar objetos Series.

'''serie1 = pd.Series([1,2,3,4,5,4,5,6])
serie2 = pd.Series([9,8,7,6,5,3,2,1])

print(serie1)
print(serie2)
print(serie1 < serie2)
print(serie1>serie2)
print(serie1 == serie2)'''

#Convertir un diccionario Python en un objeto Series
'''datos = {'a':10, 'b':20, 'c':30, 'd':40 }
serie = pd.Series(datos)
print(serie)
print(serie['a'])'''
#Convertir un arreglo NumPy en un objeto Series.
'''import numpy as np 
arreglo = np.array([1,2,3,4,5,6,7,8,9,10]) 
print(arreglo)
serie = pd.Series(arreglo)
print(serie)
print("")'''

#Cambiar el tipo de datos de un objeto Series.
'''datos = pd.Series(['100', '200', 'Python', '300.15'])
print(datos)
datos = pd.to_numeric(datos, errors = 'coerce')
print(datos)
print("")'''
#Obtener una columna de un objeto DataFrame como un objeto Series.

'''datos = [['Colombia', 'Peru', 'Chile'], ['Bolivia', 'Mexico', 'Uruguay']]
#Extraer una fila de un DataFrame como un objeto Series.
serie = pd.Series(datos)
print(serie)
serie = serie.apply(pd.Series).stack().reset_index(drop=True)
print(serie)
print("")'''

#<Ordenar los valores de un objeto Series con el método sort_values.

'''datos = ['4.5', 'Python', '0.8', 'Pandas', '2.8']
serie = pd.Series(datos)
print(serie)
serie = pd.Series(serie).sort_values()
print(serie)
print("")'''
#Agregar datos a un objeto Series existente.
'''datos = ['4.5', 'Python', '0.8', 'Pandas', '2.8']
serie = pd.Series(datos)
print(serie)
serie = serie.append(pd.Series(['Java', 'JavaScript']))
print(serie)
print("")'''

#Crear un objeto Series a partir de un 
# filtro aplicado a otro objeto Series.

datos = [1,2,3,4,5]
indices = ['A','B','C','D','E']
serie = pd.Series(data=datos, index=indices)
print(serie)
serie = serie.reindex(index=['B','A','C','D'])
print(serie)
print("")
#Obtener la desviación estándar y el promedio 
# de un conjunto de datos de una serie.

'''serie = serie.reindex(index=['B', 'A', 'C', 'D', 'A'])
print(serie)
print(serie.std())
print(serie.mean())
print("")'''

#Obtener estadísticas básicas de un objeto Series con 
# el método describe.
'''datos = list(range(10))
print(datos)
serie = pd.Series(datos)
print(serie)
print(serie.describe())
print("")'''
#Obtener los elementos pares e impares 
# de un objeto Series numérico.
'''datos = list(range(10))
print(datos)
serie = pd.Series(datos)
pares = serie[serie%2 == 0]
print(pares)
impares = serie[serie%2 != 0]
print(impares)
print("")'''

#Extraer los datos de un objeto Series como un objeto NumPy.

datos = list(range(10))
print(datos)
serie = pd.Series(datos)
print(serie)
arreglo = serie.values
print(arreglo)
print("")
