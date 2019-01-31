#Importamos la libreria de numeros aleatorios
from random import randint
#Introducir el numero de operaciones
n1=int(input("Numero de preguntas: "))
cont=0
#Validacion del apartado anterios
while n1<=0:
    print("Tiene que poner al menos 1")
    n1=int(input("Numero de preguntas: "))
#Muestra el numero de operaciones predefinidas 
for i in range(n1):
    a=randint(2,10)
    b=randint(2,10)
    n2=int(input("¿Cuanto es %d x %d?: "%(a,b)))
#Mostrar resultados
    if a*b==n2:
        print("¡Respuesta correcta!")
        cont+=1
    else:
        print("¡Respuesta incorrecta!")
#Muestra la nota final segun las respuestas
if cont==1:
    print("Ha contestado correctamente a 1 pregunta")
if cont>1:
    print("Ha contestado correctamente a %d preguntas"%cont)
print("Le corresponde una nota de %.1f"%(cont/n1*10))

