import pandas as pd

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas>=3].sort_values(ascending=True)

notas={"Juana":3.5, "lucas":2.7}

print(aprobados(notas))