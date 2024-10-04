from math import pi

# Define clase Circulo con 3 atributos
class Circulo:
    # Función constructor, se llama cuando se crea el objeto
    # El constructor define 3 atributos
    def __init__(self,radioi,centroXi,centroYi):
        self.radio=radioi
        self.centroX=centroXi
        self.centroY=centroYi

    # Se definen dos métodos para la clase Circulo
    def area(me):
        return pi*me.radio**2
    
    def perimetro(this):
        return 2*pi*this.radio

# Crea dos objetos (2 instancias) de la clase Circulo
myCircle0=Circulo(1.0,0.0,0.0)
myCircle1=Circulo(2.0,-0.1,0.1)

# Invoca métodos de la clase Circulo desde el objecto myCircle0
a=myCircle0.area()
p=myCircle0.perimetro()

print(f'El área es: {a} y el perímetro es: {p}')

# Invoca métodos de la clase Circulo desde el objecto myCircle1
a=myCircle1.area()
p=myCircle1.perimetro()

print(f'El área es: {a} y el perímetro es: {p}')


# Imprime las referencias de los objetos tipo Circulo
print(myCircle0)
print(myCircle1)

print(type(myCircle0))
print(type(3.141592654))

myCircle1.radio=float(input('Ingrese el radio del círculo '))
print(myCircle1.area())
# Imprime la clase Circulo
print(Circulo)        