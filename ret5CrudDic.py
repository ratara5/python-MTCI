def cargarEstudiante(identifiacion: int, nombre: str, edad: int, grado: str, estado: str):
    estudiantes_activos[identifiacion]=[nombre,edad,grado,estado]
    print("*Estudiante ingresado con exito*")
    print("---------------------------------")
    return estudiantes_activos

def numeroEstudiantes(estudiantes, nombre):
    for identifiacion, datos in estudiantes.items():
            if datos[0].lower() == nombre.lower():
                return(identifiacion)
    return 0

def imprimirListadoEstudiantes(estudiantes):
    for identifiacion,datos in estudiantes.items():
      print("-Número:",identifiacion)
      print("-Nombre:",datos[0])
      print("-Edad:", datos[1])
      print("-Grado:", datos[2])
      if datos[3] == "Aprobado":
          print("-Estado: Aprobado")
      else:
          print("-Estado: Reprobado")
      print("---------------------------------")

estudiantes_activos={1:["ADRIANA CAROLINA HERNÁNDEZ",14, "Décimo","Reprobado"],2:["DIANA CATALINA DIAZ",13,"Octavo","Aprobado"],3:["MARIA ALEJANDRA BOLÍVAR",13,"Décimo","Reprobado"]}
print ("---------------------------------")

print("Cargar estudiantes")
identicacionEstudiante= int (input("Ingrese ID del estudiante:  ")) # Variable para asignar la id
nombreEstudiante= str (input("Ingrese nombre del estudiante:    ")) # Variable para asignar el nombre
edadEstudiante=int (input("Ingrese edad del estudiante:  ")) # Variable para asignar la edad
gradoEstudiante=str (input("Ingrese grado del estudiante:  ")) # Variable para asignar el grado
estadoEstudiante=str (input("Ingrese estado del estudiante (Aprobado, Reprobado):  ")) # Variable para asignar el estado
estudiantes_activos=cargarEstudiante(identicacionEstudiante, nombreEstudiante,edadEstudiante,gradoEstudiante,estadoEstudiante)
print(estudiantes_activos)
print ("---------------------------------")

print("Modificar edad")
modificarEdad=int(input("Ingrese el ID del estudiante : "))
estudiantes_activos[modificarEdad][1]=int(input("Ingrese la nueva edad: "))
print ("*Estudiante :",str(estudiantes_activos[modificarEdad][0]) , ", edad actualizada con exito")
print ("---------------------------------")

print("Modificar grado")
modificarGrado=int(input("Ingrese el ID del estudiante : "))
estudiantes_activos[modificarGrado][2]=str(input("Ingrese el nuevo grado"))
print ("*Estudiante :",estudiantes_activos[modificarGrado][0] , ", grado actualizada con exito" )
print ("---------------------------------")

print("Eliminar Estudiante")
eliminarEstudiante = int(input("Ingrese el ID del estudiante : "))
nombre = estudiantes_activos[eliminarEstudiante][0]
eliminarEstudiante=numeroEstudiantes(estudiantes_activos, nombre)
if eliminarEstudiante in estudiantes_activos :
    del estudiantes_activos[eliminarEstudiante]
else:
    print ("El estudiante no se encuentra registrado")
print ("*Estudiante: ", nombre, ", eliminado con exito*")
print ("---------------------------------")

print ("Imprimiendo lista de estudiantes")
imprimirListadoEstudiantes(estudiantes_activos)