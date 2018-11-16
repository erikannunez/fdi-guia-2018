# ejercicio 28
# Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el
# número invertido. Por ejemplo, si se ingresa 1234 debe mostrar 4321.

num = int(input("Ingrese un número entero: "))
num_original = num
num_invertido = 0

while num > 0:
    num_invertido = num_invertido * 10 + (num%10)
    num = int(num/10)

print("El número %d invertido es: %d" %(num_original, num_invertido))