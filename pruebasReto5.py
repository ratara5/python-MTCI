import pandas as pd

rutas="https://raw.githubusercontent.com/JohanGordillo/CSV-Grupo-63/main/ESTUDIANTES_CASO_1.csv"
datos=pd.read_csv(rutas, header=0)
df=pd.DataFrame(datos)
# print(df)

#Da los nombres de los estudiantes en Grado1#
#for i in df["GRADO"].loc[lambda s: s==1].index:
    #print(df.NOMBRE[i])

Grado1=0
Grado2=0
Grado3=0
Grado4=0
Grado5=0

for elem in df["GRADO"]:
    if elem==1:
        Grado1 += 1
    elif elem==2:
        Grado2 += 1
    elif elem==3:
        Grado3 += 1
    elif elem==4:
        Grado4 += 1
    else:
        Grado5 += 1

print(str(Grado1))
print(str(Grado2))
print(str(Grado3))
print(str(Grado4))
print(str(Grado5))




