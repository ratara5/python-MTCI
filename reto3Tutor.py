def cargarEstudiante(identifiacion: int, nombre: str, edad: int, grado: str, estado: str):
   estudiantes_activos[identifiacion]=[nombre,edad,grado,estado]
   print ("*Estudiante ingresado con exito*")
   return estudiantes_activos

def numeroEstudiantes(estudiantes, nombre):
   for identifiacion,datos in estudiantes.items():
      if datos[0].lower()==nombre.lower():
         return identifiacion
   return 0

def imprimirListadoEstudiantes(estudiantes):
    for identifiacion,datos in estudiantes.items():
      print("-Número:",identifiacion)
      print("-Nombre:",datos[0])
      print("-Edad:",datos[1])
      print("-Grado:",datos[2])
      if datos[3] == "aprobado":
         print("-Estado: Aprobado")
      else:
         print("-Estado: Reprobado")
      print ("---------------------------------")

