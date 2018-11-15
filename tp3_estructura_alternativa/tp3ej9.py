# ejercicio 9
anio = int(input("Ingrese un año: "))
bisiesto = False

if (anio % 4 == 0):
    # podria ser bisiesto
    bisiesto = True
    if(anio % 100 == 0):
        bisiesto = False
        if(anio % 400 == 0):
            bisiesto = True
else:
    bisiesto = False

if(bisiesto):
    print("El año %d es bisiesto!" %anio)
else:
    print("El año %d no es bisiesto!" %anio)
