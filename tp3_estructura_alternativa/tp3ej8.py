# ejercicio 8
cliente = int(input("Ingrese el numero de cliente: "))
total = float(input("Ingrese el total de la factura: "))

if(total > 0):
    primeros10 = 0
    segundos10 = total
    despues20 = 0

    if (total - 120) < (total * 0.98):
        primeros10 = total * 0.98
    else:
        primeros10 = total -120

    if(total+150) > (total*1.10):
        despues20 = total+150
    else:
        despues20 = total*1.10

    print("Si paga dentro de los primeros 10 dias: $%.2f" %primeros10)
    print("Si paga entre el 11 y el 20: $%.2f" %segundos10)
    print("Si paga despues del 20: $%.2f" %despues20)

else:
    print("No hay importe para abonar.")