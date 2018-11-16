# ejercicio 32
# La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene
# como suma de los dos anteriores, siendo los dos primeros 1 y 1.
# Por lo tanto, Fib=1, 1, 2, 3, 5, 8, 13, 21.... Realizar un programa que lea N e imprima los N
# primeros términos de esta sucesión, como así también la suma de los mismos.

num = int(input("Ingrese la cantidad de terminos de la sucesión que desea mostrar: "))
while(num <= 0):
    num = int(input("Debe ingresar un número mayor a cero! Ingrese: "))

a, b = 1,1
suma = 0
for i in range(num):
    print(a, end=" | ")
    suma += a
    a, b = b, a + b

print("\nLa suma de los términos es: %d" %suma)