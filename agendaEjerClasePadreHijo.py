class Agenda:
    def __init__(self):
        self.contactos=[]

    def menu(self):
        print()
        menu=[
            ["Agenda personal"],
            ["1. Añadir contacto"],
            ["2. Lista de contactos"],
            ["3. Buscar contacto"],
            ["4. Editar contacto"],
            ["5. Cerrar agenda"]
        ]
        for elem in menu:
            print(elem[0])
        opcion=int(input("Introduzca el número de la opción deseada: "))
        if opcion==1:
            self.anadir()
        elif opcion==2:
            self.lista()
        elif opcion==3:
            self.buscar()
        elif opcion==4:
            self.editar()
        else:
            print("Saliendo de la agenda...")
            exit()
        self.menu()

    def anadir(self):
        print("*"*20)
        print("Añadir nuevo contacto")
        print("*"*20)
        nom=input("Introduzca el nombre: ")
        tel=int(input("Introduzca el teléfono: "))
        email=input("Introduzca el e-mail: ")
        self.contactos.append({"nombre": nom,
                               "teléfono": tel,
                               "email": email})

    def lista(self): #solo los nombres, con ellos podremos buscar luego un contacto
        print("*" * 20)
        print("Lista de contactos")
        print("*" * 20)
        if len(self.contactos)==0:
            print("No hay ningún contacto en la lista")
        else:
            for dic in self.contactos:
                print(dic["nombre"])

    def buscar(self):
        print("*" * 20)
        print("Buscar un contacto")
        print("*" * 20)
        name=input("Introduzca el nombre del contacto a buscar: ")
        for dic in self.contactos:
            if name==dic["nombre"]:
                print("Datos del contacto")
                print("nombre: "+dic["nombre"])
                print("teléfono: "+str(dic["teléfono"]))
                print("email: "+dic["email"])
                return self.contactos.index(dic)

    def editar(self):
        print("*" * 20)
        print("Editar contacto")
        print("*" * 20)
        data=self.buscar()
        condicion=False
        while condicion==False:
            print("Seleccione que quiere editar: ")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. Email")
            print("4. Volver")
            opcion= int(input("Introduzca la opcion deseada: "))
            if opcion==1:
                nom=input("Introduzca un nuevo nombre")
                self.contactos[data]["nombre"]=nom
            elif opcion==2:
                tel = input("Introduzca un nuevo teléfono")
                self.contactos[data]["teléfono"] = tel
            elif opcion==3:
                email = input("Introduzca un nuevo e-mail")
                self.contactos[data]["email"] = email
            elif opcion==4:
                condicion=True

agenda=Agenda()
agenda.menu()




