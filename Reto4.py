def listaEstudiante(Dictionary):
    print("Base de datos estudiantes \n")
    print("------------------------")
    for value in Dictionary.values():
        print("Nombre:          "+value[0])
        print("Apellido:        " + value[1])
        print("Nota:  " + str(value[2]))
        print("------------------------")

def notas_estudiantes(Dictionary):
    print("Rangos de notas de estudiantes")
    R5 = 0  # Los que sacaron entre 0 y 20
    R4 = 0  # Los que sacaron entre 21 y 40
    R3 = 0  # Los que sacaron entre 41 y 60
    R2 = 0  # Los que sacaron entre 61 y 80
    R1 = 0  # Los que sacaron entre 81 y 99
    R0 = 0  # Los que sacaron 100
    for value in Dictionary.values():
        if value[2]>=0 and value[2]<=20:
            R5+=1
        elif value[2] >= 21 and value[2] <= 40:
            R4+=1
        elif value[2] >= 41 and value[2] <= 60:
            R3 += 1
        elif value[2] >= 61 and value[2] <= 80:
            R2 += 1
        elif value[2] >= 81 and value[2] <= 99:
            R1 += 1
        else:
            R0 += 1
    cadena="los que sacaron entre "
    print(cadena+"0 a 20:  "+str(R5)+"  estudiantes")
    print(cadena + "21 a 40:  " + str(R4)+"  estudiantes")
    print(cadena + "41 a 60:  " + str(R3)+"  estudiantes")
    print(cadena + "61 a 80:  " + str(R2)+"  estudiantes")
    print(cadena + "81 a 90:  " + str(R1)+"  estudiantes")
    print("Nota perfecta:  "+str(R0)+"  estudiantes")
    print("------------------------")


Diccionario={
            1:["JUAN PABLO", "MÉNDEZ", 10],
            2:["JUAN", "ACOSTA", 37],
            3:["MAICOL LEANDRO", "RUIZ GACHA", 48],
            4:["ANA LORENA", "ALVARADO", 80],
            5:["DEIBIS ALEJANDRO", "CABEZA MENDOZA", 91],
            6:["SARA VALENTINA", "GAVIRIA", 100],
            7:["KAREN DAYANNA", "SÁNCHEZ", 51],
            8:["WILL ALEXANDER", "CANTILLO", 72],
            9:["JUAN SEBASTIÁN", "LEÓN", 63],
            10:["JHOAN STIVEN", "CHAMORRO", 43],
            11:["GARY JESÚS", "PADILLA", 82],
            12:["ANDRÉS", "ACOSTA", 32],
            13:["LUISA FERNANDA", "ARGUELLES", 84],
            14:["JOHAN SEBASTIÁN", "ÁLVAREZ", 62],
            }
notas_estudiantes(Diccionario)
listaEstudiante(Diccionario)


###########POR CAPRICHO#################
def notas_estudiantes(estudiantes):
    listaEntre0_20 = 0
    listaEntre21_40 = 0
    listaEntre41_60 = 0
    listaEntre61_80 = 0
    listaEnetre81_99 = 0
    listaPerfecto = 0

    for identifiacion, datos in estudiantes.items():
        if datos[2] >= 0 and datos[2] < 20:
            listaEntre0_20 += 1
        elif datos[2] >= 21 and datos[2] < 40:
            listaEntre21_40 += 1
        elif datos[2] >= 41 and datos[2] < 60:
            listaEntre41_60 += 1
        elif datos[2] >= 61 and datos[2] < 80:
            listaEntre61_80 += 1
        elif datos[2] >= 81 and datos[2] < 99:
            listaEnetre81_99 += 1
        elif datos[2] == 100:
            listaPerfecto += 1

    print("Rango de notas de estudiantes  \n"
          "Los que sacaron entre 0 a 20: ", listaEntre0_20, " estudiantes\n"
                                                            "Los que sacaron entre 21 a 40: ", listaEntre21_40,
          " estudiantes\n"
          "Los que sacaron entre 41 a 60: ", listaEntre41_60, " estudiantes\n"
                                                              "Los que sacaron entre 61 a 80: ", listaEntre61_80,
          " estudiantes\n"
          "Los que sacaron entre 81 a 99: ", listaEnetre81_99, " estudiantes\n"
                                                               "Nota perfecta: ", listaPerfecto, " estudiantes")
    print("---------------------------------")


def listaEstudiante(estudiantes):
    print("Base de datos estudiantes")
    print("---------------------------------")
    for identifiacion, datos in estudiantes.items():
        print("Nombre:         ", datos[0], "\n"
                                            "Apellido:       ", datos[1], "\n"
                                                                          "Nota: ", datos[2])
        print("---------------------------------")
