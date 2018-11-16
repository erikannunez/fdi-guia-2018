# ejercicio 24
# El factorial de un número entero N mayor que cero se define como el producto
# de todos los enteros X tales que 0 < X <= N. Desarrollar un programa para cal-
# cular el factorial de un número dado. Deberán rechazarse las entradas inválidas
# (menores que 0).

num = int(input("Ingrese un número entero mayor o igual a cero: "))
while(num < 0):
    num = int(input("Debe ingresar un número mayor o igual a cero! Ingrese: "))

#iniciamos en 1 porque vamos a multiplicar
factorial = 1
# recorremos desde 1 hasta el numero ingresado inclusive
for i in range(1,num+1): #tambien podriamoso poner range(num) y luego factorial *= (i+1) en la linea siguiente
    factorial *= i


print("!%d = %d" %(num,factorial))