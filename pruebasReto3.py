estudiantes_activos={1:["ADRIANA CAROLINA HERNÁNDEZ",14, "Décimo","Reprobado"],2:["DIANA CATALINA DIAZ",13,"Octavo","Aprobado"],3:["MARIA ALEJANDRA BOLÍVAR",13,"Décimo","Reprobado"]}
a=list(enumerate(estudiantes_activos.values()))
print(a)
nombre="diana catalina diaz"
for tup in a:
    for elem in tup[1]:
        if tup[1][0].upper() == nombre.upper():
            print(tup[0]+1)

def numeroEstudiantes(estudiantes, nombre):
    for identifiacion, datos in estudiantes.items():
            if datos[0].upper() == nombre.upper():
                return(identifiacion)
    return 0

# listaAtributos=["ID","nombre","edad","grado","estado"]
# listaVariables=[]
# for i in range(0,len(listaAtributos)):
#     listaVariables.append(input("Por favor ingrese "+listaAtributos[i]+": "))
#
# dic={int(listaVariables[0]):listaVariables[1:5]}
#
# print(dic)
#
