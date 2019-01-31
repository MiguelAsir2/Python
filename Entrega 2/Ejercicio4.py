l1=[]
n1=int(input("Cuantas palabras tiene la lista: "))
for i in range(1,n1+1):
    pal=input("Dime la palabra %d: "%i)
    while len(pal)<=1:
        print("La palabra tiene que tener más de un caracter")
        pal=input("Dime la palabra %d: "%i)
    l1.append(pal)
print("La lista creada es: %s"%l1)
while True:
    print('''
Menú

1. Contar
2. Modificar
3. Eliminar
0. Salir''')
    n2=int(input("Elija una opcion: "))
    if n2==1:
        print("1. Contar")
        pal1=input("Digame la palabra a buscar: ")
        if l1.count(pal1)==1:
            print("La palabra '%s' aparece una vez en la lista" %pal1)
        elif l1.count(pal1)>1:
            print(" La palabra '%s' aparece %d veces en la lista"%(pal1,l1.count(pal1)))
        else:
            print("La palabra '%s' no aparece en la lista"%pal1)
    elif n2==2:
        print("2. Modificar")
        pal1=input("Sustituir la palabra: ")
        pal2=input("por la palabra: ")  
        for i in range(l1.count(pal1)):
            l1.remove(pal1)
            l1.append(pal2)
        print(l1)
    elif n2==3:
        print("3. Eliminar")
        pal1=input("Palabra a eliminar: ")
        for i in range (l1.count(pal1)):
            l1.remove(pal1)
        print("Lalista es ahora: %s"%l1)
    elif n2==0:
        break
    else:
        print("Ese número no pertenece a ninguna opción.")
print("Hasta la próxima.")