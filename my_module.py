from math import sqrt

class PiFormulas:
    def __init__(self,n):
        self.n=n

    def formula1(self):        
        acc=0.0
        x=-1
        step=2.0/self.n
        for i in range(0,self.n):
            acc+=step*sqrt(1.0-x**2)
            x+=step            
        return 2.0*acc


def factorial(n):
    p=1
    for i in range(n):
        p=p*(i+1)
    return p

            

