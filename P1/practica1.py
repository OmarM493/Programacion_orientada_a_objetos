"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

area = calcular_area_rectangulo(2, 5)

print("El area del rectangulo es:", area)



#Implementar el paradigma Orientado a Objetos (OO)

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

rect = Rectangulo(2, 5)

print("El area del rectangulo es:", rect.area())

#Implementar el paradigma Orientado a Objetos (OO)
class Rectangulos:
    def area(self,base,altura):
        areaR=base*altura
        return areaR

rectangulo1=Rectangulos() #Crear o instanciar un objeto "rectangulo1" de la clase "Rectangulos"
print(f"El area del rectangulo  es: {rectangulo1.area(5,6)}")