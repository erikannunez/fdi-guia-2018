# ejercicio 27
# Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
# Ejemplo: Si se ingresa 12345 debe imprimir 5.

num = int(input("Ingrese un número entero: "))
num_original = num
digitos = 1

#tenemos que "castear" la división a int porque por defecto se transforma en float al dividir
while int(num/10) > 0:
    num = int(num/10)
    digitos += 1

print("El número %d tiene %d dígitos!" %(num_original, digitos))