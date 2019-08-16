#Manuel David Quiceno Gallego
#Juan Pablo Muñoz Muñoz
#1
print("hello world")
print("")
#2
variable = "hello world"
#3
print(type(variable))
print("")
#4
variable = variable.replace(" world", "")
#5
def oddNumbersOneToTwenty(lista):
    for i in lista:
        if i % 2 != 0:
            print(i)
    print("")
oddNumbersOneToTwenty(range(1,21))
#6
from my_tools import ex as exponecial
def exponentiation(lista, potencia):
    return exponecial(lista,potencia)
print(exponentiation([2,3,4,5],2))
print("")
#7
diccionario = {"variableUno": [1,2,3,4], "variableDos": ["1","a","?"]}
#8
spam = "Spam"
spam.replace("S","Z")
print(spam)
print("")
#9
def perimeterOfARectangle(x, y):
    return 2*x + 2*y
print(perimeterOfARectangle(2,2))
print("")
#10
class person:
    def __init__(self, estatura, peso):
        self.estatura = estatura 
        self.peso = peso
    def BMI(self):
        return self.peso/(self.estatura**2)

manuel = person(1.62,30) 
juan = person(1.74,65)
andres = person(1.67,55)
quintana = person(1.81,63)
andrea = person(1.67,44)
lista = [manuel, juan, andres, quintana, andrea]

def calcBMI(listaa):
    for i in listaa:
        print(i.BMI())     
    print("")
calcBMI(lista)
#11
def printsNumbers():
    for i in range(1,101):
        mensaje = ""
        if i % 2 == 0:
            mensaje += "whiz "
        if i % 3 == 0:
            mensaje += "bang "
        if (i % 2 != 0) & (i % 3 != 0):
            print(repr(i))
        else:
            print(mensaje)
printsNumbers()
print("")