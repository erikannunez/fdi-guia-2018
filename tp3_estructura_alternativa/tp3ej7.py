# ejercicio 7
cantVendida = int(input("Ingrese la cantidad vendida: "))
precioBase = float(input("Ingrese el precio base: "))
totalVenta = 0

if cantVendida > 0 and precioBase > 0:

    if cantVendida <= 12:
        totalVenta = precioBase * cantVendida
    elif cantVendida > 12 and cantVendida <= 100:
        totalVenta = (precioBase*12) + (cantVendida-12)*(precioBase*0.90)
    else:
        totalVenta = (precioBase*12) + (88 * (precioBase*0.90)) + (cantVendida-100)*(precioBase*0.75)
    print("El valor total de la venta es: $%.2f" %totalVenta)
    print("El precio promedio es de: $%.2f" %(totalVenta/cantVendida))
else:
    print("No se han vendido unidades o no se ha determinado el precio.")