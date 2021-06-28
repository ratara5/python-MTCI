import pandas as pd
import numpy as np

em6=pd.read_csv('C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/inf_2016.csv')
em7=pd.read_csv('C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/inf_2017.csv')
em8=pd.read_csv('C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/inf_2018.csv')
em9=pd.read_csv('C:/Users/TabSan/Desktop/Programación UTP/Programación/Unidad 5/Archivos/inf_2019.csv')

#Generar un DataFrame con los datos de los cuatro ficheros.
em=pd.concat([em6,em7,em8,em9])
print(em)

# Filtrar las columnas del DataFrame para quedarse con las columnas ESTACION, MAGNITUD, AÑO, MES
# y las correspondientes a los días D01, D02, etc.
columnas=['ESTACION','MAGNITUD','ANO','MES',]
columnas.extend([col for col in em if col.startswith('D')])
em = em[columnas]
em
print(em)

# Reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días aparezcan en una
# única columna.
em=em.melt(id_vars=['ESTACION','MAGNITUD','ANO','MES'], var_name='DIA', value_name='VALOR')
em.DIA=em.DIA.str.strip('D')
em
print(em)

# Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día (usar el módulo datetime).
em['FECHA']=em.ANO.apply(str)+'/'+em.MES.apply(str)+'/'+em.DIA.apply(str)
em['FECHA'] = pd.to_datetime(em.FECHA, format='%Y/%m/%d', infer_datetime_format=True, errors='coerce')
em
print(em)

# Eliminar las filas con fechas no válidas (utilizar la función isnat del módulo numpy) y ordenar el DataFrame por estaciones, contaminantes y fecha.
em=em.drop(em[np.isnat(em.FECHA)].index)
em.sort_values(['ESTACION','MAGNITUD','FECHA'])

# Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame.
print('Estaciones: ',em.ESTACION.unique())
print('Contaminantes: ',em.MAGNITUD.unique())

# Crear una función que reciba una estación, un contaminante y un rango de fechas y devuelva una serie con
# las emisiones del contaminante dado en la estación y rango de fechas dado.
def evolucion(estacion, contaminante, desde, hasta):
    return em[(em.ESTACION == estacion) & (em.MAGNITUD == contaminante) & (em.FECHA >= desde) & (em.FECHA <= hasta)].sort_values('FECHA').VALOR
# evolucion(56, 8, dt.datetime.strptime('2018/10/25', '%Y/%m/%d'), dt.datetime.strptime('2019/02/12', '%Y/%m/%d'))

# Mostrar un resumen descriptivo (mímino, máximo, media, etc) para cada contaminante.

print(em.groupby(['MAGNITUD']).VALOR.describe())

# Mostrar un resumen descriptivo para cada contaminente por distritos.
print(em.groupby(['ESTACION','MAGNITUD']).VALOR.describe())

# Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del
# contaminante indicado en la estación indicada.
def emisiones(estacion, contaminante):
    return em[(em.ESTACION==estacion) & (em.MAGNITUD==contaminante)].VALOR.describe()
print(emisiones(4,8))
# Resumen de Dióxido de Nitrógeno en Plaza Elíptica
print('Resumen Dióxido de Nitrógeno en Plaza Elíptica:\n', emisiones(56, 8),'\n', sep='')

# Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todos las
# estaciones.
def emimedmen(contaminante, ano):
    return em[(em.MAGNITUD==contaminante)&(em.ANO==ano)].groupby(['ESTACION','MES']).VALOR.mean().unstack('MES')
print(emimedmen(1,2015))

# Crear un función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos
# tipos de contaminantes.

def medmencon(estacion):
    return em[(em.ESTACION==estacion)].groupby(['ANO','MAGNITUD','MES']).VALOR.mean().unstack('MAGNITUD')

print(medmencon(35))