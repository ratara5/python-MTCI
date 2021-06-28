import pandas as pd

def estudiantes(rutas):

    datos=pd.read_csv(rutas, header=0)
    df=pd.DataFrame(datos)

    listaEntre0_20 = 0
    listaEntre21_40 = 0
    listaEntre41_60 = 0
    listaEntre61_80 = 0
    listaEntre81_99 = 0
    listaPerfecto = 0

    for prom in df["PROMEDIO"]:
        if prom >= 0 and prom <=20:
            listaEntre0_20 += 1
        elif prom >= 21 and prom <=40:
            listaEntre21_40 += 1
        elif prom >= 41 and prom <=60:
            listaEntre41_60 += 1
        elif prom >= 61 and prom <=80:
            listaEntre61_80 += 1
        elif prom >= 81 and prom <=99:
            listaEntre81_99 += 1
        else:
            listaPerfecto += 1

    diccionarioPromedios={"Entre 0 a 20": listaEntre0_20,
                         "Entre 21 a 40": listaEntre21_40,
                         "Entre 41 a 60": listaEntre41_60,
                         "Entre 61 a 80": listaEntre61_80,
                         "Entre 81 a 99": listaEntre81_99,
                         "Perfecto": listaPerfecto
                         }
    Grado1 = 0
    Grado2 = 0
    Grado3 = 0
    Grado4 = 0
    Grado5 = 0

    for elem in df["GRADO"]:
        if elem == 1:
            Grado1 += 1
        elif elem == 2:
            Grado2 += 1
        elif elem == 3:
            Grado3 += 1
        elif elem == 4:
            Grado4 += 1
        else:
            Grado5 += 1

    diccionarioGrados={"Grado 1": Grado1,
                       "Grado 2": Grado2,
                       "Grado 3": Grado3,
                       "Grado 4": Grado4,
                       "Grado 5": Grado5
                       }

    return diccionarioPromedios, diccionarioGrados

# https://github.com/JohanGordillo/CSV-Grupo-63
print(estudiantes("https://raw.githubusercontent.com/JohanGordillo/CSV-Grupo-63/main/ESTUDIANTES_CASO_2.csv"))