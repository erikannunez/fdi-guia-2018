# ejercicio 25
# Leer dos números naturales A y B. Calcular A^B mediante productos sucesivos y
# mostrar el resultado. Tener en cuenta que A y B pueden ser nulos.

numA = int(input("Ingrese un número entero A >= 0: "))
while(numA < 0):
    numA = int(input("Debe ingresar un número A >= 0! Ingrese: "))

numB = int(input("Ingrese un número entero B >= 0: "))
while(numB < 0):
    numB = int(input("Debe ingresar un número B >= 0! Ingrese: "))

resultado = 1
for i in range (numB):
    resultado *= numA

print("%d^%d = %d" %(numA,numB,resultado))
