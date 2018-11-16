# ejercicio 19
# Leer un conjunto de números que representan edades de un grupo de personas,
# finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son
# menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de
# ambos grupos.

menor18 = 0
mayor18 = 0
sumaEdades = 0
edad = int(input("Ingrese edad [1-120]: "))
while edad != 999:
    if edad > 0 and edad <= 120:
        if edad < 18:
            menor18 += 1
        else:
            mayor18 +=1
        sumaEdades += edad
        edad = int(input("Ingrese edad [1-120]: "))
    else:
        edad = int(input("Edad fuera de rango! Ingrese nuevamente: "))

print("Menores de 18 años: %d" %menor18)
print("18 años o más: %d" %mayor18)
print("Promedio edades: %.2f" %(sumaEdades/(menor18+mayor18)))