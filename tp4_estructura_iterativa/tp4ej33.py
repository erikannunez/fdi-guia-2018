# ejercicio 33
# La raíz cuadrada de un número positivo n puede calcularse mediante la siguiente fórmula de Newton:
# donde a es una aproximación a . Al aplicar repetidamente esta fórmula reemplazando a
# por la aproximación obtenida en el paso anterior, se obtiene cada vez
# una aproximación mejor. Desarrollar un programa que calcule la raíz cuadrada
# aproximada de un número entero positivo n, utilizando como primera aproximación a n/2.
# Detener el proceso cuando la diferencia entre dos cálculos sucesivos sea menor a 0,0001.

def raiz(num):
    aprox=num/2 #inicializamos la primer aproximacion como n/2
    error=(aprox**2)-num #calculamos el error existente
    while(error >= 0.0001): #mientras el error sea mayor o igual a 0.0001
        aprox = ((num/aprox)+aprox)/2 #formula de newton
        error = (aprox**2)-num #el nuevo error sera el cuadrado de la aproximacion menos el numero ingresado
    return aprox #devolvemos la raiz aproximada

num = int(input("Ingrese un número entero mayor o igual a cero: "))
while(num < 0):
    num = int(input("Debe ingresar un número mayor o igual a cero! Ingrese: "))

print("La raiz de %d es : %.4f" %(num,raiz(num)))