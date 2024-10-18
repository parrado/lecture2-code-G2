from math import pi

# Base/parent class is abstract
class Shape:
    def __init__(self,centerX,centerY):
        self.centerX=centerX
        self.centerY=centerY
    
    # area must be implementd by child classes 
    # (polymorphism)
    def area(self):
        pass

# Circle inherits from Shape
class Circle(Shape):
    
    def __init__(self,centerX,centerY,radius):
        super().__init__(centerX,centerY)
        self.radius=radius
        

    def area(self):
        return pi*self.radius**2

# Triangle inherits from Shape
class Triangle(Shape):
    def __init__(self,centerX,centerY,base,height):
        super().__init__(centerX,centerY)
        self.height=height
        self.base=base
        

    def area(self):
        return self.base*self.height/2
    
# Object Circle of radius 1    
myCircle0=Circle(-2.0,2.0,1.0)

# Object Triangle of base 5 and heigh 3
myTriangle0=Triangle(0.1,0.1,5.0,3.0)

aCircle=myCircle0.area()
aTriangle=myTriangle0.area()

print(f'El área del círculo es: {aCircle}')
print(f'El área del triángulo es: {aTriangle}')
print(f'Coordenadas del centro del círculo: {(myCircle0.centerX,myCircle0.centerY)}')
print(f'Coordenadas del centro del triángulo: {(myTriangle0.centerX,myTriangle0.centerY)}')

