print("DIVISORES DE NUMEROS")
#Programa. Introduce dos números e indica su resultado
#Introduce el dividendo y el divisor
dividendo=int(input("Introduce el dividendo: "))
divisor=int(input("Introduce el divisor: "))
#Validacion del divisor.
while divisor==0:
    print("Error.No se puede dividir por Cero")
    divisor=int(input("Introduce el divisor: "))
#Posibles resultados
if dividendo%divisor==0:
    print("La division es exacta. Cociente: %d"%(dividendo/divisor))
if dividendo%divisor!=0:
    print("La division no es exacta. Cociente: %d Resto: %d"%(dividendo/divisor,dividendo%divisor))
