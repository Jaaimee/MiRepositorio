import math
# def suma(x, y):
#     print(f"La suma de {x} y {y} es: {x + y}")
# def resta(x, y):
#     print(f"La resta entre {x} y {y} es: {x - y}")
suma = lambda x, y: x + y
resta = lambda x, y: x - y

o=0

while (o!=12):
    print("CALCULADORA")
    print("1.Suma de dos números")
    print("2.Resta de dos números")
    print("3.Multiplicación de dos números")
    print("4.División de dos números")
    print("5.Cociente de dos números")
    print("6.Resto de la división de dos números")
    print("7.Exponente de dos números")
    #Añadimos áreas a nuestra calculadora científica
    print("8.- Área de un triángulo")
    print("9.- Área de un rectángulo")
    print("10.- Área de un círculo")
    print("11.- Área de un cuadrado")
    o=int(input("Introduzca uno de los números anteriores para elegir operación: "))
    if (o == 1):
        x=int(input("Escribe el primer número: "))
        y=int(input("Escribe el segundo número: "))
        print(suma(x, y))
        
    elif (o == 2):
        x=int(input("Escribe el primer número: "))
        y=int(input("Escribe el segundo número: "))
        print(resta(x, y))
    break
    
    