##Función que permite obtener el ahorro consolidado de la familia Gordillo
#Entradas -> pJ: dinero aportado por Juan (float)
#Variables -> pX: dinero aportado por Xiomara (float), pM: dinero aportado por #Melissa (float)

def dinero(pJ: float)-> str:
    pX=pJ/2 #Calcular dinero aportado por Xiomara
    pM=(pJ+pX)/2 #Calcular dinero aportado por Melissa
    total=pJ+pX+pM #Calcular dinero total aportado
    return "La familia tiene un ahorro de: ${}".format(total) #devolver dinero #total aportado

print(dinero(40000))
print(dinero(60000))
print(dinero(70000))


def dinero(pesosJohan: float) -> str:
    pesosXiomara = pesosJohan / 2
    pesosMelissa = (pesosJohan + pesosXiomara) / 2
    total = pesosJohan + pesosXiomara + pesosMelissa
    return "La familia tiene un ahorro de : ${} ".format(total)


print(dinero(40000))
print(dinero(60000))
print(dinero(70000))