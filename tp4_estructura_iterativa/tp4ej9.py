#ejercicio 9
# Realizar un programa para ingresar desde el teclado un conjunto de números.
# Mostrarlos a medida que se los ingresa. Finalizar la lectura de datos con el valor -1.

num = int(input("Ingrese un número. -1 para salir: "))

while(num != -1):
    print(num)
    num = int(input("Ingrese un número. -1 para salir: "))