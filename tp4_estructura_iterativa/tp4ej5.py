# ejercicio 5
# Leer dos números A y B enteros positivos. Calcular el producto A * B por sumas
# sucesivas e imprimir el resultado. Ejemplo: 4 * 3 = 4 + 4 + 4 (4 sumado 3 veces).

numA = int(input("Ingrese un número entero positivo: "))
numB = int(input("Ingrese otro número entero positivo: "))
producto = 0

if(numA >= 0 and numB >= 0):
    for i in range(numB):
        producto += numA
    print("%d * %d = %d" %(numA,numB,producto))
else:
    print("Los números ingresados deben ser positivos!")