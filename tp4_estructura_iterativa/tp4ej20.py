# ejercicio 20
# Leer A y B enteros positivos y verificar que A >= B. Una vez hecha esta verifica-
# ción, dividir A sobre B mediante restas sucesivas, es decir sin utilizar el operador
#
# de división. Ejemplo 5 dividido 2:
# · Restamos el dividendo menos el divisor: 5 - 2 = 3
# · Repetimos esta resta tantas veces como sea posible: 3 - 2 = 1
# · Al ser el resultado (1) menor que el divisor (2), detenemos el proceso.
# · Este resultado es el resto de la división, mientras que el cociente se
#
# obtiene contando la cantidad de restas que se efectuaron. Imprimir divi-
# dendo, divisor, cociente y resto.

numA = int(input("Ingrese número A: "))
while numA <= 0:
    numA = int(input("El número debe ser positivo! Ingrese número A: "))

numB = int(input("Ingrese número B: "))
while numB <= 0:
    numB = int(input("El número debe ser positivo! Ingrese número B: "))

if numA >= numB:
    dividendo = numA
    divisor = numB
    resto = dividendo
    cociente = 0

    while resto >= divisor:
        cociente += 1
        if resto-divisor >= 0:
            resto -= divisor

    print("Dividendo: %d" %dividendo)
    print("Divisor: %d" %divisor)
    print("Cociente: %d" %cociente)
    print("Resto: %d" %resto)

else:
    print("A debe ser mayor o igual a B. %d es menor que %d. Intente nuevamente." %(numA,numB))