# ejercicio 4
# Leer diez números enteros e imprimir el mayor.

contar = 1
mayor = 0

while (contar <=10):
    num = int(input("%d. Ingrese un número: "%contar))
    contar += 1
    if(num > mayor):
        mayor = num

print("El mayor de los números ingresados es el %d" %mayor)


