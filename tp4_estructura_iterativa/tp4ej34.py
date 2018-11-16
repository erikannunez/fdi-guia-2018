# ejercicio 34
# Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y
# un número entero N que representa una cantidad de días. Realizar un programa
# que calcule e imprima la nueva fecha que resulta de sumar N días a la fecha
# dada. Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 9 de
# la práctica 3.

def is_bisiesto(anio):
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
    return bisiesto

def is_fecha_valida (dia, mes, anio):
    fechaValida = True
    if(dia > 0 and dia <= 31) and (mes > 0 and mes <=12) and anio > 0:
        if (dia == 31 and (mes != 1 or mes != 3 or mes != 5 or mes != 7 or mes != 8 or mes != 10 or mes != 12)) \
                or (dia == 30 and (mes != 4 or mes != 6 or mes != 9 or mes != 11)) \
                or (dia == 28 and mes == 2 and is_bisiesto(anio)) \
                or (dia == 29 and mes == 2 and not is_bisiesto(anio)):
            fechaValida = False
    else:
        fechaValida = False
    return fechaValida

dia = int(input("Ingrese un día [1-31]: "))
while(dia <= 0 or dia > 31):
        dia = int(input("El rango de dias es [1-31]! Ingrese nuevamente: "))
mes = int(input("Ingrese un mes [1-12]: "))
while(mes <= 0 or mes > 12):
        mes = int(input("El rango de meses es [1-12]! Ingrese nuevamente: "))
anio = int(input("Ingrese un año: "))
while(anio <= 0):
        anio = int(input("El año debe ser positivo! Ingrese nuevamente: "))

if is_fecha_valida(dia,mes,anio):
    cantDias = int(input("Ingrese cantidad de días a sumar a la fecha: "))
    while(cantDias < 0):
        cantDias = int(input("Debe ingresar un entero positivo! Ingrese: "))
    # comenzamos con la suma de dias

newDia = dia
newMes = mes
newAnio = anio
for i in range(1,cantDias+1):
# TODO terminar funcion
else:
    print("La fecha ingresada no es válida! Fin del programa.")


