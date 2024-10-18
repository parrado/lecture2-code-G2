# Importa el módulo creado
#from my_module import PiFormulas
#from my_module import factorial
import my_module

# Crea un objeto tip piFormulas
o=my_module.PiFormulas(10000)

#Invoca métdodo formula1
print(o.formula1())

print(my_module.factorial(10))