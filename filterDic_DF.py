
#26/05/2021 con esta rutina se crea un diccionario de nombres con características (nombres, puntajes...), se transforma
# dicho diccionario en un dataframe. De dicho dataframe se extrae otro dataframe cuyas filas cumplen determinados
# valores, en este caso puntajes>=6.

import pandas as pd
import numpy as np

def multiple(numero):
    if numero<6:
        return True

nombres = ["David", "Juan", "Esteban", "Raymond", "Johan", "Pacho"]
puntajes = [9.3, 2.3, 4.6, 8.6, 1.2, 4.6]
intentos = [1, 3, 4, 2, 1, 0]
calificado = ["si", "no", "si", "no", "no", "no"]

jugadores = {
    'nombres': nombres,
    'puntajes': puntajes,
    'intentos': intentos,
    'calificado': calificado,
}

df=pd.DataFrame(jugadores)
# print(df)
npPuntajes=np.array(jugadores["puntajes"]) #Crear arreglo Numpy con los puntajes llamado npPuntajes
iM6=list(np.nonzero(npPuntajes>=6))[0] #Extraer del arreglo npPuntajes los índices de los mayores o iguales a 6,
# colocarlos en una lista; [0] es el primer elemento (que también es una lista) de dicha lista.
# print(iM6)
filtro_iM6=df.iloc[iM6] #Extraer nuevo dataframe
print("La siguiente es la lista de aprobados:")
print(filtro_iM6)


