# Reto Unidad 2
# La UTP desea hacer un evento para sus colaboradores,
# para ello talento humano pide averiguar el signo zodiacal de cada trabajador,
# para de esta manera entregar un detalle con el concepto de los signos zodiacales.
# Para este proceso se pide que cada colaborador ingrese en una aplicación su día
# y mes de nacimiento, y este muestre por pantalla el signo zodiacal que tiene el usuario.

# Si el día o mes, no se encuentra en estos rangos establecidos debe mostrar al usuario
# el siguiente mensaje:  " Fecha incorrecta “

def ingresodatos():
    dia=int(input("Ingrese el día de nacimiento (número entero del 1 al 31) -> "))
    mes=int(input("Ingrese el mes de nacimiento (número entero del 1 al 12) -> "))
    return dia,mes

def durames(month): #Entrada número del mes en el año (1 a 12), Salida duración del mes (28, 30, 31)
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        durmes=31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        durmes=30
    else:
        durmes=28
    return durmes

def agredurprimes(vector):
    ms=vector[2]
    dm=durames(ms)
    vector[1]=dm
    return vector

diamesCapricornio=[22,0,12,1,20,1]
diamesAcuario=[21,0,1,1,19,2]
diamesPiscis=[20,0,2,1,20,3]
diamesAries=[21,0,3,1,20,4]
diamesTauro=[21,0,4,1,21,5]
diamesGeminis=[22,0,5,1,21,6]
diamesCancer=[22,0,6,1,23,7]
diamesLeo=[24,0,7,1,23,8]
diamesVirgo=[24,0,8,1,23,9]
diamesLibra=[24,0,9,1,23,10]
diamesEscorpion=[24,0,10,1,22,11]
diamesSagitario=[23,0,11,1,21,12]
diamesTotal=[diamesCapricornio,diamesAcuario, diamesPiscis, diamesAries, diamesTauro,diamesGeminis,diamesCancer, diamesLeo,diamesVirgo, diamesLibra, diamesEscorpion, diamesSagitario]

for i in range(0,len(diamesTotal)): #Agregar a cada vector de días, el día final de cada mes inicial
    agredurprimes(diamesTotal[i])

diamesTotal={'Capricornio':diamesCapricornio,'Acuario':diamesAcuario, 'Piscis':diamesPiscis, 'Aries':diamesAries, 'Tauro':diamesTauro,'Geminis':diamesGeminis,'Cancer':diamesCancer, 'Leo':diamesLeo,'Virgo':diamesVirgo, 'Libra':diamesLibra, 'Escorpion':diamesEscorpion, 'Sagitario':diamesSagitario}
keys=diamesTotal.keys()
print(keys)

while True:
    d,m=ingresodatos()
    diamesUsuario=[d,m]
    duramonth = durames(m)
    if (m>12 or m<1) or (d>duramonth or d<1):
        print ("Fecha incorrecta")
        d, m = ingresodatos()

    for keys in diamesTotal:
        mi=diamesTotal[keys][2]
        di=diamesTotal[keys][0]
        mf=diamesTotal[keys][5]
        df=diamesTotal[keys][4]
        if m==mi and d>=di or m==mf and d<=df:
            print("su signo es " + str(keys))
            break