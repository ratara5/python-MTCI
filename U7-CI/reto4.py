def notas_estudiantes(estudiantes):
 
   listaEntre0_20 = 0
   listaEntre21_40 = 0
   listaEntre41_60 = 0
   listaEntre61_80 = 0
   listaEnetre81_99 = 0
   listaPerfecto = 0
   
   for identifiacion,datos in estudiantes.items():
      if datos[2] >= 0 and datos[2]< 20:
         listaEntre0_20 += 1
      elif datos[2] >= 21 and datos[2] < 40:
         listaEntre21_40 += 1
      elif datos[2] >= 41 and datos[2] < 60:
         listaEntre41_60 += 1
      elif datos[2] >= 61 and datos[2] < 80:
         listaEntre61_80 += 1
      elif datos[2] >= 81 and datos[2] < 99:
         listaEnetre81_99 += 1
      elif datos[2] == 100 :
         listaPerfecto += 1                                              
   
   print("Rango de notas de estudiantes  \n" 
        "Los que sacaron entre 0 a 20: " , listaEntre0_20 , " estudiantes\n"
        "Los que sacaron entre 21 a 40: " , listaEntre21_40 , " estudiantes\n"
        "Los que sacaron entre 41 a 60: " , listaEntre41_60 , " estudiantes\n"
        "Los que sacaron entre 61 a 80: " , listaEntre61_80 , " estudiantes\n"
        "Los que sacaron entre 81 a 99: " , listaEnetre81_99 , " estudiantes\n"
        "Nota perfecta: " , listaPerfecto , " estudiantes")
   print("---------------------------------")

def listaEstudiante(estudiantes):
    print("Base de datos estudiantes")
    print("---------------------------------")
    for identifiacion,datos in estudiantes.items():
    	print("Nombre:         " , datos[0] , "\n"
           	"Apellido:       " , datos[1] , "\n"
            "Nota: " , datos[2])
    	print("---------------------------------")


usuarios_grado_11 = {
					0:[
								"JUAN PABLO",
								"MENDEZ",
								10
								],
					1:[
								"JUAN",
								"ACOSTA",
								37
								],
     				2:[
								"MAICOL LEANDRO",
								"RUIZ GACHA",
								48
								],
					3:[
								"ANA LORENA",
								"ALVARADO",
								80
								],
     				4:[
								"DEIBYS ALEJANDRO",
								"CABEZA MENDOZA",
								91
								],
					5:[
								"SARA VALENTINA",
								"GAVIRIA",
								100
								],
     				6:[
								"KAREN DAYANNA",
								"SANCHEZ",
								51
								],
					7:[
								"WILL ALEXANDER",
								"CANTILLO",
								72
								],
     				8:[
								"JUAN SEBASTIAN",
								"LEON",
								63
								],
					9:[
								"JHOAN STYVEN",
								"CHAMORRO",
								43
								],
     			   10:[
								"GARY JESUS",
								"PADILLA",
								82
								],
					11:[
								"ANDRES ",
								"ACOSTA",
								32
								],
     				12:[
								"LUISA FERNANDA",
								"ARGUELLES",
								84
								],
					13:[
								"JOHAN SEBASTIAN ",
								"ALVAREZ",
								62
								]
			}

notas_estudiantes(usuarios_grado_11)
listaEstudiante(usuarios_grado_11)