# ejercicio 23
# Leer un número natural M. Calcular e imprimir:
# · La sumatoria de los números naturales menores o iguales que M.
# · La productoria de los números naturales mayores o iguales que M y menores que M*2.

c
sumatoria = 0
productoria = 1 #inicia en uno para no multiplicar por cero
#recorremos del 1 al doble del natural inclusive. Ej: ingreso 10 => recorre del 1 al 20
for i in range(1, (natural*2)+1):
    if(i <= natural):
        sumatoria += i
    elif i >= natural:
        productoria *= i
    else:
        continue

print("Sumatoria: %d | Productoria: %d" %(sumatoria,productoria))