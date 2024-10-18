class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # Define age como una propiedad de solo lectura
    @property
    def age(self):
        return self.__age

    # Con el setter se puede tener control de qué valores
    # son válidos para la propiedad
    @age.setter
    def age(self,age):
        if age>=0:
            self.__age=age
    
    # Método para imprimir nombre
    def sayHi(self):
        print(f'Hi I\'m {self.name}')

cadena=input('Ingrese el nombre: ')    
p0=Person(cadena,33)
p1=Person('Cristina',20)
p0.sayHi()
p0.age=19
print(p0.age)
        