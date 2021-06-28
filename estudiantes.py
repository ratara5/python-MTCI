Estudiantes={1:{"Nombre":"ALFONSO","Apellido":"NOREÑA","Notas":[]}}
print(Estudiantes)

#Función para crear  registro
def leerEstudiante():
    print("Crear estudiante")
    identificacionEstudiante= int (input("Ingrese id del estudiante:  ")) # Variable para asignar la id
    nombreEstudiante= str (input("Ingrese nombre del estudiante:    ")) # Variable para asignar el nombre
    apellidoEstudiante = str(input("Ingrese apellido del estudiante:    "))  # Variable para asignar el nombre
    return identificacionEstudiante, nombreEstudiante, apellidoEstudiante

#Funcion para cargar un estudiante al diccionario Estudiantes
def cargarEstudiante(identificacion: int, nombre: str, apellido: str):
    Estudiantes.update({identificacion:{}})
    Estudiantes[identificacion]["Nombre"]=nombre
    Estudiantes[identificacion]["Apellido"]=apellido
    print ("*Estudiante ingresado con exito*")
    print("---------------------------------")

#Función para cargar  notas
def cargarNotas(identif: int):
    print("Cargar notas")
    Notas=[]
    for i in range (1,11):
        n=float(input("Por favor ingrese Nota "+str(i)+ ": "))
        Notas.append(n)
    Estudiantes[identif]["Notas"]=Notas
    print("---------------------------------")

while True:
    identificacionEstudiante, nombreEstudiante, apellidoEstudiante=leerEstudiante()
    cargarEstudiante(identificacionEstudiante, nombreEstudiante, apellidoEstudiante)
    cargarNotas(identificacionEstudiante)
    print(Estudiantes)