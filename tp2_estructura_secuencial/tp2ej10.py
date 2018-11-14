# ejercicio 10
dinero = int(input("Ingrese monto a extraer: "))

billetes100 = int(dinero/100)
billetes50 = int((dinero%100)/50)
billetes10 = int(((dinero%100)%50)/10)
billetes5 = int((((dinero%100)%50)%10)/5)
billetes1 = int(((((dinero%100)%50)%10)%5)/1)

print("Billetes $100: %d" %billetes100)
print("Billetes $50: %d" %billetes50)
print("Billetes $10: %d" %billetes10)
print("Billetes $5: %d" %billetes5)
print("Billetes $1: %d" %billetes1)