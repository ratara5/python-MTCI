class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Crear objeto1
persona1 = Persona('Juan', 24)
print(persona1.nombre)
print(persona1.edad)
print(id(persona1))
# Crear objeto2
persona2 = Persona('Melissa', 2)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))

#
class Aritmetica:

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2

    def dividir(self):
        return self.operando1 / self.operando2


# crear objeto1
aritmetica1 = Aritmetica(4, 2)
print('La suma es: ', aritmetica1.sumar())
print('La resta es: ', aritmetica1.restar())
print('La multiplicación es: ', aritmetica1.multiplicar())
print('La división es: ', aritmetica1.dividir())

# crear objeto2
aritmetica2 = Aritmetica(8, 5)
print('La suma es: ', aritmetica2.sumar())
print('La resta es: ', aritmetica2.restar())
print('La multiplicación es: ', aritmetica2.multiplicar())
print('La división es: ', aritmetica2.dividir())


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input('Prporcione la base: '))
altura = int(input('Proporcione la altura: '))

# Crear el objeto
rectangulo = Rectangulo(base, altura)

print(rectangulo.calcular_area())


class Caja:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo


ancho = int(input('Proporcione el ancho: '))
alto = int(input('Proporcione el alto: '))
profundo = int(input('Proporcione lo profundo: '))

# Crear objeto
caja = Caja(ancho, alto, profundo)

print('El volumen de la caja es: ', caja.calcular_volumen())


# n=nombre, e=edad, *v= valores tupla, **d= diccionario
class Persona:
    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d

    def desplegar(this):
        print("El nombre es: ", this.nombre)
        print('La edad es: ', this.edad)
        print('Los valores de la tupla: ', this.valores)
        print('Los valores del diccionario: ', this.diccionario)

    def parOImpar(this):
        if this.edad%2==0:
            return print("la edad es par")
        else:
            return print("la edad es impar")

p1 = Persona('Juan', 24)
p1.desplegar()
print()

p2 = Persona('Melissa', 2, 1, 2, 3, )
p2.desplegar()
print()

p3 = Persona('Elizabeth', 57, 7, 8, 9, m='Manzana', p='Pera', u='Uva')
p3.desplegar()
p3.parOImpar()
print()

p4 = Persona('Numero', int(input("ingresar número: ")))
p4.desplegar()
p4.parOImpar()



