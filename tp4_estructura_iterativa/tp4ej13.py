# Realizar un programa para ingresar desde el teclado un conjunto de números e
# informar los elementos ingresados menores a un valor ingresado previamente.
# Finalizar la lectura de datos con el valor -1.

inicio = int(input("Ingrese un valor contra el cual se comparará: "))
num = int(input("Ingrese un número (-1 para terminar): "))
while(num != -1):
    if num < inicio:
        print("%d es menor a %d" %(num,inicio))
    num = int(input("Ingrese un número (-1 para terminar): "))