
from coches import *

# print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
# coche1.getInfo()


# print("Objeto 2")
# coche2=Coches("Azul","Nissan","2020",180,160,6)
# coche2.getInfo()

print(coche1.publico_atributo)
#print(coche1.__privado_atributo) Esto no es permitido
print(coche1.getPrivadoAtributo())

#coche1.__getMetodoPrivada() Esto no es permitido
coche1.getMetodoPublico()



