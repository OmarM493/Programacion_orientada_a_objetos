"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares
#Muestre el color de los coches 
#que los operaciones disminuyan o aumneten la velocidad segun sea el caso y hay que jugar con ellos e imprimes la velocidad final


class Coches:
    marca=""
    color="Sin color"
    velocidad=0
    potencia=0
    asientos=0

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

#Multiples objetos
coche1=Coches()
coche2=Coches()

print(f"el color del coche 1 es: {coche1.color}")
coche1.color="Rojo y blanco"
print(f"el color del coche 1 es: {coche1.color}")
coche2.color="Negro y blanco"
print(f"el color del coche 2 es: {coche2.color}")
print(f"El velocidad final del coche es: {coche1.velocidad}")
for i in range(1,11):
    coche1.acelerar()
print(f"El velocidad final del coche es: {coche1.velocidad}")
