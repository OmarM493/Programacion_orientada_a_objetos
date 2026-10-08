#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches, Camiones, Camionetas

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

camion1=Camiones("Negro", "Dina", "2020", 180, 300, 12, 8, 2500)
camion2=Camiones("Azul", "Star", "2019", 150, 200, 14, 6, 2000)


camioneta1=Camionetas("Amarillo","Renault","2025",240,250,8,"delantera",True)
camioneta2=Camionetas("Blanca","Nissan","2020",180,150,0,"trasera",False)
