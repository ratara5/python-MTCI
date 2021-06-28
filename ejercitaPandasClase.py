# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla
# una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento
# del 10%.

import pandas as pd

inicio = int(input("Digite año inicial: "))
fin = int(input("Digite año final: "))

ventas = {}

for i in range(inicio, fin + 1):
    ventas[i] = float(input("Introduzca la venta del año: " + str(i) + ": "))

ventas = pd.Series(ventas)
print("ventas:\n", ventas)
print("ventas con descuento:\n", ventas * 0.9)

# Escribir una función que reciba un diccionario con las notas de los alumnos en curso en un examen y
# devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadistico = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index = ['Min', 'Max', 'Media', 'Desviasión Típica'])
    return estadistico

notas = {"Melissa": 2.5, "Juan": 3.5, "Elizabeth":5.0, "Carolina": 1.0}
print(estadistica_notas(notas))

#otra

import pandas as pd

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas>=3].sort_values(ascending=True)

notas = {"Juan": 3.5, "Alejandra": 2.5, "Eliana": 4.8}
print(aprobados(notas))

#otra

import pandas as pd
import numpy as np

datos = [['Medellín',1800,23], ['Bogotá',2600,13], ['Cartagena',20,35], ['Bello',1700,26]]
meteorologia = pd.DataFrame(datos, columns=['Ciudad', 'msnm_prom','Temp_prom'])
print(meteorologia)
print(meteorologia.mean())
print(list(np.array(pd.Series(meteorologia.mean())))) # se han transformado en lista los promedios

#otro
import numpy as np
import pandas as pd

matToDf=pd.DataFrame(np.random.randn(3,3),columns=['A','B','C'],index=('a','b','c')) #objeto matriz numpy aleatorio a dataframe
print(matToDf)

print(matToDf.apply(lambda x: x.max() - x.min())) #Mayor - menor por columna
print(matToDf.apply(lambda x: x.max() - x.min(),1)) #Mayor - menor por fila

# Escribir una función que reciba una diccionario con las notas de los alumnos en curso en un examen y devuelva
# una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

import pandas as pd
def notasAprobados(dic):
    print(pd.Series(dic)[pd.Series(dic)<=3].sort_values(ascending=True))

notas={'Abdías':3, 'Beto':2.5, 'Caro':3.7, 'Dalai':5}
notasAprobados(notas)

#Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente
import pandas as pd
df=pd.DataFrame([['Enero',30500,22000],['Febrero',35600,23400],['Marzo',28300,18100],['Abril',33900,2070]],index=[x for x in range(0,4)],columns=['Mes','Ventas','Gastos'])

df["Balance"]=df.Ventas-df.Gastos

print(df[df.Balance>=30000])
