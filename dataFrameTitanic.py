# Ejercicio 1
# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:
# •	Generar un DataFrame con los datos del fichero.
# •	Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
# •	Mostrar por pantalla los datos del pasajero con identificador 148.
# •	Mostrar por pantalla las filas pares del DataFrame.
# •	Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
# •	Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
# •	Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
# •	Eliminar del DataFrame los pasajeros con edad desconocida.
# •	Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
# •	Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
# •	Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
import pandas as pd

#•	Generar un DataFrame con los datos del fichero.
titanic = pd.read_csv('C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/titanic.csv', index_col=0)
print(titanic)

#•	Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas
# y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas

print('La dimensión es: ', titanic.shape)
print('El número de elementos es: ', titanic.size)
print('El nombre de las columnas son:', titanic.columns)
print('Las filas son: ', titanic.index)
print('Tipos de datos: ', titanic.dtypes)
print('Primeras 10 filas: ', titanic.head(10))
print('Últimas 10 filas: ', titanic.tail(10))

#•	Mostrar por pantalla los datos del pasajero con identificador 148.
#print(titanic.loc[148])

#•	Mostrar por pantalla las filas pares del DataFrame.
print(titanic.iloc[range(1,titanic.shape[0],2)])

#•	Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
print(titanic[titanic['Pclass']==1]['Name'].sort_values())

#•	Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print(titanic['Survived'].value_counts()/titanic['Survived'].count()*100)

#•	Mostrar por pantalla el porcentaje de personas que muririeron sobrevivieron en cada clase.
print(titanic.groupby('Pclass')['Survived'].value_counts(normalize=True))

# •	Eliminar del DataFrame los pasajeros con edad desconocida.
titanic.dropna(subset=['Age'])

#•	Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print(titanic.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])

#•	Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
titanic['Young'] = titanic['Age']<18
print(titanic)

#•	Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.

print(titanic.groupby(['Pclass','Young'])['Survived'].value_counts(normalize= True))

