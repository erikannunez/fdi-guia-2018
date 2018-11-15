# ejercicio 15
# Realizar un programa para ingresar desde el teclado un conjunto de números y
# mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
# con un valor -1.

mayor = 0
menor = 0
num = int(input("Ingrese un número (-1 para terminar): "))
while(num != -1):
    if(num > mayor):
        mayor = num
    if(num < menor):
        menor = num
    num = int(input("Ingrese un número (-1 para terminar): "))

print("El mayor de los números ingresados es el %d" %mayor)
print("El menor de los números ingresados es el %d" %menor)

