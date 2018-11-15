# ejercicio 11
# Realizar un programa para ingresar desde el teclado un conjunto de números e
# informar si la cantidad de elementos es impar o par, sin utilizar contadores.
# Finalizar la lectura de datos con el valor -1.

num = int(input("Ingrese un numero: "))
#creamos una lista donde vamos a guardar los numeros ingresados
numeros = []

while(num != -1):
    numeros.append(num)
    num = int(input("Ingrese un numero: "))

if(len(numeros)%2 == 0):
    print("La cantidad de elementos ingresada fue par! Se ingresaron %d elementos." %len(numeros))
else:
    print("La cantidad de elementos ingresada fue impar! Se ingresaron %d elementos." % len(numeros))