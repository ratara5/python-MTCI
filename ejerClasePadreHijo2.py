'''Desarrollar un programa que conste de una clase padre Cuenta y dos 
subclases PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad
y un método para imprimir los datos en la clase Cuenta. La clase CajaAhorro
tendrá un método para heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un
método para obtener el importe del interés (cantidad*interés/100) y otro 
método para mostrar la información, datos del titular plazo, interés y 
total de interés.Crear al menos un objeto de cada subclase.'''

#creamos clase Cuenta
class Cuenta:
    #inicializamos los atributos de la clase
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    #imprimimos los datos
    def imprimir(self):
        print ("Tutular: ", self.titular)
        print ("Cantidad: ",self.cantidad)
   
#crear una clase CajaAhorro
#Esta clase hereda atributos de la clase cuenta
class CajaAhorro(Cuenta):
    
    #inicializamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
        
    #imprimimos los datos de la cuenta
    def imprimir(self):
        print("Cuenta de caja de ahorro")
        super().imprimir()
        
#Creamos la clase PazoFijo
#Esta clase tambien hereda los atributos de la clase cuenta
class PlazoFijo(Cuenta):
    
    #inicializamos los atributos de la clase 
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo = plazo
        self.interes = interes 
        
    #calcular la ganacia
    def ganacia(self):
            ganacia = self.cantidad * self.interes / 100
            print("El importe del interes es " , ganacia)
            
    #imprimimos los resultados
    def imprimir(self):
        print("Cuenta plazo fijo")
        super().imprimir()
        print ("Plazo disponible en dias: ",self.plazo)
        print ("Interes: ", self.interes)
        self.ganacia()
        
      
caja1=CajaAhorro("Juan",8000) 
caja1.imprimir()    
        
plazo1=PlazoFijo("Johan", 10000, 365, 1.6)
plazo1.imprimir()
