def durames(month: int): #Entrada número del mes en el año (1 a 12), Salida duración del mes (28, 30, 31)
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        durmes=31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        durmes=30
    else:
        durmes=28
    return durmes
x=durames(10)
print("el mes"+" dura "+str(x)+" días")
