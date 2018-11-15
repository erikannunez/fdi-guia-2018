# ejercicio 6
# Leer diez números e imprimir el menor de ellos, indicando además el número de
# orden con que fue leído.
contar = 1
menor = 0
orden = 0

while (contar <=10):
    num = int(input("%d. Ingrese un número: "%contar))

    if(num < menor):
        menor = num
        orden = contar

    contar += 1
print("El menor de los números ingresados es el #%d: %d" %(orden,menor))

