class Vehiculo():
    def __init__(self, color, rueda):
        self.color = color
        self.rueda = rueda
        
    def __str__(self):
        return "El color es {}, {} ruedas".format(self.color, self.rueda)
    
class Coche(Vehiculo):
    def __init__(self, color, rueda, velocidad, cilindrada):
        self.color = color
        self.rueda = rueda
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return "el color {}, {} ruedas, {} km/h, {} cc ".format(self.color, self.rueda, self.velocidad, self.cilindrada)
    
#Crear el objeto
coche1 = Coche("Azul", 4, 150, 1200)
print(coche1)

coche2 = Coche("Negro", 4, 260, 2500)
print(coche2)
