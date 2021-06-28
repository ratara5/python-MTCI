# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado.
# La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
# los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva
# deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un
# inmueble se calcula con las siguiente fórmula en función de la zona:

import pandas as pd

dicCasas=[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

df=pd.DataFrame(dicCasas)

df["precio"] = (df.metros * 1000 + df.habitaciones * 5000 + df.garaje * 15000) * (2021 - df.año) / 100

#df[df["zona"]=='B']['precio']=df[df["zona"]=='B']['precio']*1.5

for i in df["zona"].loc[lambda s: s=="B"].index:
    df.precio[i]=df.precio[i]*1.5

print(df)
