#Crear el diccionario y rellenar con los datos
estudiantes_activos={1:["ROBIN HOOD"], 2:["ALBERT EINSTEIN"], 3:["PETER PARKER"]}

#Funcion para cargar un estudiante al diccionario estudiantes_activos
def cargarEstudiante(identifiacion: int, nombre: str):
    estudiantes_activos[identifiacion]=[nombre]
    print ("*Estudiante ingresado con exito*")
    print("---------------------------------")

#Función para crear  registro
def leerEstudiante():
    print("Crear estudiante")
    identicacionEstudiante= int (input("Ingrese id del estudiante:  ")) # Variable para asignar la id
    nombreEstudiante= str (input("Ingrese nombre del estudiante:    ")) # Variable para asignar la nombre
    cargarEstudiante(identicacionEstudiante, nombreEstudiante)

#Funcion para mostrar a todos los estudiantes
def imprimirListadoEstudiantes(estudiantes):
    for identifiacion,datos in estudiantes.items():
      print("-Número:",identifiacion)
      print("-Nombre:",datos[0])
      print ("---------------------------------")

#Función para modificar registro
def modificarEstudiante():
    print ("modificar nombre")
    numeroEstudiante = int(input("Ingrese el ID del estudiante : "))
    estudiantes_activos[numeroEstudiante][0] = str(input("ingrese nuevo nombre : "))
    print("Estudiante : ",estudiantes_activos[numeroEstudiante][0])
    print("---------------------------------")

#Función para eliminar registro
def eliminarEstudiante():
    print ("eliminar nombre")
    numeroEstudiante = int(input("Ingrese el ID del estudiante : "))
    del estudiantes_activos[numeroEstudiante]
    print("Estudiante: "+str(numeroEstudiante)+" eliminado con éxito")
    print("---------------------------------")

while True:
    opcion=int(input("Seleccione una opción \n1: Crear \n2: Mostrar \n3: Modificar \n4: Eliminar\n"))
    if opcion == 1:
        leerEstudiante()
    if opcion == 2:
        imprimirListadoEstudiantes(estudiantes_activos)
    if opcion == 3:
        modificarEstudiante()
    if opcion == 4:
        eliminarEstudiante()