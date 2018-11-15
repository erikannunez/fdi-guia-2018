# ejercicio 14
# Realizar un programa para ingresar desde el teclado un conjunto de números e
# informar en forma separada la cantidad de elementos pares e impares ingresa-
# dos. Finalizar la lectura de datos con el valor -1.

pares = 0
impares = 0
num = int(input("Ingrese un número (-1 para terminar): "))
while(num != -1):
    if num%2 == 0:
        pares += 1
    else:
        impares += 1
    num = int(input("Ingrese un número (-1 para terminar): "))

print("Se ingresaron %d números pares y %d números impares" %(pares,impares))