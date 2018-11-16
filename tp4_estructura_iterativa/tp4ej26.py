# ejercicio 26
# Calcular e imprimir la suma de los números enteros comprendidos entre dos
# números enteros A y B ingresados por teclado. Tener en cuenta que A puede ser
# mayor, menor o igual que B.

numA = int(input("Ingrese un número entero: "))
numB = int(input("Ingrese un número entero: "))
suma = 0

#como queremos los numeros que están entre A y B, arrancamos desde A+1 para no incluirlo
for i in range(numA+1,numB):
    suma += i

print("La suma es: %d" %suma)