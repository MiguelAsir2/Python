print("COMPARACIÓN DE TRES NÚMEROS")
# Introducir los datos con los que vamos a operar
n1=int(input("Escriba un número: "))
n2=int(input("Escriba otro número: "))
n3=int(input("Escriba otro número: "))
#Resultados segun su condicion
if n1==n2 and n2==n3 and n1==n3:
    print("Ha escrito tres veces el mismo número")
elif n2==n3 or n1==n3 or n2==n1:
    print("Ha escrito uno de los números dos veces")
else:
    print("Los tres números que ha escrito son distintos")
