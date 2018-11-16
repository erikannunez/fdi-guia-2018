# ejercicio 21
# Leer un número natural N. Calcular e imprimir los números naturales pares menores que N.

natural = int(input("Ingrese un número natural (entero positivo): "))
while(natural <= 0):
    natural = int(input("Debe ingresar un entero positivo! Ingrese: "))

for i in range(1, natural):
    if i%2 == 0:
        print(i)