print("MAYORES QUE EL PRIMERO")
#Introduce el numero de repeticiones
n1=int(input("¿Cuantos valores vas a introducir?: "))
#Validar el numero de repeticion
while n1<=0:
    print("¡Imposible!")
n2=int(input("Escriba un numero: "))
#Bucle que nos indica una condicion
for i in range(n1):
    n3=int(input("Escriba un numero mayor que %d: "%n2))
    if n3<=n2:
        print("¡%d no es mayor que %d!"%(n3,n2))
print("Gracias por su colaboracion")