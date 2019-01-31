print("COMPARADOR DE AÑOS")
#Programa. Introduce dos años y te indica la diferencia
#Introduce los datos
año_actual=int(input("¿En que año estamos?: "))
año_cualquiera=int(input("Escriba un año cualquiera: "))
#Operacion para calcular la diferencia de año
b=año_cualquiera-año_actual
#Condiciones para mostrar los resultados
if año_actual==año_cualquiera:
    print("¡Son el mismo año!")
if año_actual<año_cualquiera and b>1:
    print("Para llegar al año %d faltan %d años"%(año_cualquiera,b))
# Muestra el resultado en singular
elif año_actual<año_cualquiera and b==1:
    print("Para llegar al %d falta %d año"%(año_cualquiera,b))
if año_actual>año_cualquiera and abs(b)>1:
    print("Desde el año %d han pasado %d años"%(año_cualquiera,abs(b)))
#Muestra el resultado en singula
elif año_actual>año_cualquiera and abs(b)==1:
    print("Desde el año %d ha pasado %d año"%(año_cualquiera,abs(b)))