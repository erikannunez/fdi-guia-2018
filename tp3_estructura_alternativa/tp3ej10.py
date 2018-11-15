# ejercicio 10
l1 = float(input("Ingrese longitud lado 1: "))
l2 = float(input("Ingrese longitud lado 2: "))
l3 = float(input("Ingrese longitud lado 3: "))

#lado mayor = a
#lados restantes = b y c
a,b,c = 0,0,0

if (l1 == l2 and l2 == l3) or (l1 >= l2 and l1 >= l3):
    a,b,c = l1,l2,l3
elif l2 >= l1 and l2 >= l3 :
    a,b,c = l2,l1,l3
elif l3 >= l1 and l3 >= l2 :
    a,b,c = l3,l1,l2
else:
    a,b,c = l1,l2,l3

print("A: %d | B: %d | C: %d" %(a,b,c))

if(a >= b + c):
    print("No es un triángulo!")
elif a**2 == b**2 + c**2:
    print("Se trata de un triángulo rectángulo!")
elif a**2 > b**2 + c**2:
    print("Se trata de un triángulo obtusángulo!")
elif a**2 < b**2 + c**2:
    print("Se trata de un triángulo acutángulo!")
else:
    print("Triángulo desconocido O.O")

