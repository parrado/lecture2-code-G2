class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    
    # Método para imprimir nombre
    def sayHi(self):
        print(f'Hi I\'m {self.name}')

cadena=input('Ingrese el nombre: ')    
p0=Person(cadena,33)
p1=Person('Cristina',20)
p0.sayHi()
p0.age=-45
print(p0.age)
        