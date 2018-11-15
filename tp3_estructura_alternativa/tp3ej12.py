# ejercicio 12
dia = int(input("Ingrese un día [1-31]: "))
mes = int(input("Ingrese un mes [1-12]: "))
anio = int(input("Ingrese un año: "))
fechaValida = True
bisiesto = False

#tenemos que verificar si el año era bisiesto
if (anio % 4 == 0):
    # podria ser bisiesto
    bisiesto = True
    if (anio % 100 == 0):
        bisiesto = False
        if (anio % 400 == 0):
            bisiesto = True
else:
    bisiesto = False

if(dia > 0 and dia <= 31) and (mes > 0 and mes <=12) and anio > 0:
    if (dia == 31 and (mes != 1 or mes != 3 or mes != 5 or mes != 7 or mes != 8 or mes != 10 or mes != 12)) \
            or (dia == 30 and (mes != 4 or mes != 6 or mes != 9 or mes != 11)) \
            or (dia == 28 and mes == 2 and bisiesto) \
            or (dia == 29 and mes == 2 and not bisiesto):
        fechaValida = False
        print("La fecha %d/%d/%d no es válida!" % (dia, mes, anio))
    else:
        print("La fecha %d/%d/%d es válida!" % (dia, mes, anio))
else:
    print("Los datos ingresados deben ser positivos y deben encontrarse dentro del rango indicado!!")