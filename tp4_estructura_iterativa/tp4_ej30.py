# ejercicio 30
# Leer un número natural N. Calcular e imprimir los primeros N términos de la
# sucesión geométrica de razón 3, cuyos primeros términos son 1, 3, 9, 27, 81.....
# es decir 3^0, 3^1, 3^2, 3^3....
natural = int(input("Ingrese un número natural (entero positivo): "))
while(natural <= 0):
    natural = int(input("Debe ingresar un entero positivo! Ingrese: "))

for i in range(natural):
    print("Término #%d: %d" %(i+1,3**i))