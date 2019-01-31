cad1=input("Introduce una cadena: ")
indi=False
for i in cad1:
   if cad1.count(i)>1:
       indi=True
if indi:
    print("Hay caracteres repetidos")
else:
    print("No hay caracteres repetidos")