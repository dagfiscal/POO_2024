# El while es una estructura de control repetitiva o ciclica que funciona con iteraciones X veces siempre y cuando la condicion sea "True"

# Sintaxi: 

# while condicion:
#     bloque instrucciones

#Ejemplo 1 Crear un programa que imprima 5 veces el caracter @

contador=1
while contador<=5:
    print("@")
    contador+=1

#Ejemplo 2 Crear un programa que imprima los numeros del 1 a 5, los sume e imprima la suma al final
suma=0
contador=1
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es: {suma}")


# Ejemplo 3 Crear un programa que solicite un numero entero y apartir de este numero genere e imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese un numero: "))

multi=0
i=1
while i<=10:
    multi=numero*i
    print(f"{numero} X {i} = {multi}")
    i+=1
    




 


    
