# ejercicio 12
# Realizar un programa para ingresar desde el teclado un conjunto de números e
# informar el último elemento ingresado en una posición par. Finalizar la lectura de
# datos con el valor -1.
# Ejemplos:
# Si la secuencia es 3 7 4 5 6 7 9 -1 el valor a informar es 7
# Si la secuencia es 3 7 4 5 -1 el valor a informar es 5

num = int(input("Ingrese un número (-1 para terminar): "))
contar = 0
ultimo = 0
posicion = 0
while(num != -1):
    contar +=1
    if(contar%2 == 0):
        ultimo = num
        posicion = contar
    num = int(input("Ingrese un número (-1 para terminar): "))

print("El último elemento ingresado en una posición par fue el %d, que se ingresó en la %d posición." %(ultimo,posicion))

# ----------------------- #
# otra forma de hacerlo - #
# con listas ------------ #
# ------------------------#
numeros = []
num_b = int(input("Ingrese un número (-1 para terminar): "))
ultimo_b = 0
posicion_b = 0
while(num_b != -1):
    numeros.append(num_b)
    num_b = int(input("Ingrese un número (-1 para terminar): "))

if len(numeros)%2 == 0:
    posicion_b = len(numeros)
    ultimo_b = numeros[-1]
else:
    posicion_b = len(numeros)-1
    ultimo_b = numeros[-2]

print("El último elemento ingresado en una posición par fue el %d, que se ingresó en la %d posición." %(ultimo_b,posicion_b))