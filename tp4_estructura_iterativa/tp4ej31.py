# ejercicio 31
# Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es primo o no.
# Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad.

natural = int(input("Ingrese un número natural (entero positivo): "))
while(natural <= 0):
    natural = int(input("Debe ingresar un entero positivo! Ingrese: "))

divisores = 0
for i in range(1,natural+1):
    if natural%i == 0:
        divisores += 1 #contamos la cantidad de divisores del numero ingresado

#un numero primo solo puede tener dos divisores
if divisores == 2:
    print("El número %d ES PRIMO!" %natural)
else:
    print("El número %d NO ES PRIMO!" %natural)