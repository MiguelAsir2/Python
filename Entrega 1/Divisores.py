print("DIVISORES")
#Introduce el dato con el que vamos a operar
n1=int(input("Escriba un número mayor que cero: "))
#Validacion
while n1<=0:
    print("¡Le he pedido un número mayor que cero!")
    n1=int(input("Escriba un número mayor que cero: "))
#Imprime el resultado en una linea
print("Los divisores de %d son : "%n1,end="")
for i in range (1,n1):
    if n1%i==0:
        print(i," ",end="")
print(n1)
