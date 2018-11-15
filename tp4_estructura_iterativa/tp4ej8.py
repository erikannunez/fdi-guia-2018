# ejercicio 8
# Leer diez números e imprimir el mayor, el menor y el rango del conjunto
# (El rango de un conjunto se calcula restando el mayor menos el menor).

contar = 1
mayor = 0
menor = 0

while (contar <=10):
    num = int(input("%d. Ingrese un número: "%contar))
    contar += 1
    if(num > mayor):
        mayor = num
    if(num < menor):
        menor = num

print("El mayor de los números ingresados es el %d" %mayor)
print("El menor de los números ingresados es el %d" %menor)
print("El rango del conjunto es %d" %(mayor-menor))
