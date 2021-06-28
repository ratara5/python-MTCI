import pandas as pd
import numpy as np


nombres = ["David", "Juan", "Esteban", "Raymond", "Johan"]
puntajes = [9.3, 2.3, 4.6, 8.6, 1.2]
intentos = [1, 3, 4, 2, 1]
calificado = ["si", "no", "si", "no", "no"]
indices = ["a", "b", "c", "d", "e"]

jugadores = {
    'nombres': nombres,
    'puntajes': puntajes,
    'intentos': intentos,
    'calificado': calificado,
}

df = pd.DataFrame(data=jugadores, index=indices)
# print(df)
print("")
# print(df.iloc[0:3]['nombres'])
listaNombres=df.iloc[:]['nombres'].tolist()
listaPuntajes=df.iloc[:]['puntajes'].tolist()
print(listaNombres,listaPuntajes)

indiceBorrar=[]

for i in range(0,len(listaPuntajes)):
    if listaPuntajes[i]<=6.0:
        indiceBorrar.append(i)

for elem in indiceBorrar:
    listaPuntajesNew=np.delete(listaPuntajes, indiceBorrar)
    listaNombresNew=np.delete(listaNombres, indiceBorrar)


dicNew={'nombres':listaNombresNew, 'puntajes':listaPuntajesNew}
print(dicNew)

dfNew = pd.DataFrame(data=dicNew) #¿Cómo hacer para dejarlos con los índices iniciales?
print(dfNew.iloc[:])

