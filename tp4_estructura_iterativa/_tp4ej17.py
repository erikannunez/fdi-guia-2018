# ejercicio 17
# Para las mismas series del ejercicio anterior, informar el término de mayor valor
# que sea menor a un tope ingresado previamente. Ejemplo: Para las series a), b) y c),
# si se ingresa el valor 10 como tope se deberá informar 9, 10 y 7 respectivamente.
tope = int(input("Ingrese valor tope: "))
# A
base = 2
exponente = 0
num = 0
mayor_a = 0
anterior_a = 0
for i in range(20):

    if base == 2:
        num = base**exponente
        base +=1
    else:
        num = base**exponente
        base -= 1
        exponente +=1
    print(num)
    if(num > anterior_a):
        anterior_a = num
    if(anterior_a < tope):
        mayor_b = anterior_a

print("El numero mayor de A que es menor al tope es: %d" %mayor_a)
# B
mayor_b = 0
for i in range(20):
    num = ((i+1)*(-1)**(i+1))
    print(num)
    if num < tope:
        mayor_b = num
print("El numero mayor de B que es menor al tope es: %d" %mayor_b)
# C
anterior = 1
mayor_c = 0
for i in range(20):
    num = anterior + i
    anterior += i
    print(num)
    if num < tope:
        mayor_c = num
print("El numero mayor de C que es menor al tope es: %d" %mayor_c)