#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches

coche1=Coches("VW","BLANCO","2022",220,150,5)
coche2=Coches("Nissan","AZUL","2020",180,150,6)

# coche1.acelerar()
# coche1.acelerar()
print(coche1.getVelocidad())
for i in range(1,101):
    coche1.acelerar()
print(coche1.getVelocidad())

coche1.setVelocidad(400)
print(coche1.getVelocidad())