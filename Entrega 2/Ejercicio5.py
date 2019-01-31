l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
n1 = int(input("Cuantas palabras tiene la primera lista: "))
if n1 != 0:
    for i in range(1, n1+1):
        cad1 = input("Digame la palabra %d: " % i)
        l1.append(cad1)
    if l1.count(cad1) > 1:
        l1.remove(cad1)
    print("La primera lista es: %s" % l1)
else:
    print("Imposible. Lista vacia")
n1 = int(input("Cuantas palabras tiene la segunda lista: "))
if n1 != 0:
    for i in range(1, n1+1):
        cad2 = input("Digame la palabras %d: " % i)
        l2.append(cad2)
    if l2.count(cad2) > 1:
        l2.remove(cad2)
    print("La segunda lista es: %s" % l2)
    print("Palabras que aparecen en las dos listas: ", end="")
    for cad1 in l1:
        for cad2 in l2:
            if cad1 == cad2:
                l3.append(cad1)
    print(l3, "", end="")
    print()
    print("Las palabras que aparecen en la primera lista son: ", end="")
    for cad1 in l1:
        if cad1 not in l2:
            l4.append(cad1)
            print(l4,end="")
    print()
    print("Las palabras que aparecen en la segunda lista son: ", end="")
    for cad2 in l2:
       if cad2 not in l1:
           l5.append(cad2)
           print(l5,end="")
    print()
    print("Todas las palabras: %s"%(l3+l4+l5))
else:
    print("Imposible. La lista esta vacia")
