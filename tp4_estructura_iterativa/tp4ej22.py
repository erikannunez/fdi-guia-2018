# ejercicio 22
# Leer un número natural N. Calcular e imprimir los primeros N números naturales impares.

natural = int(input("Ingrese un número natural (entero positivo): "))
while(natural <= 0):
    natural = int(input("Debe ingresar un entero positivo! Ingrese: "))

contador = 0
i = 1
while contador < natural:
    # si es impar lo imprimimos e incrementamos el contador
    if i%2 != 0:
        print(i)
        contador+=1
    i += 1