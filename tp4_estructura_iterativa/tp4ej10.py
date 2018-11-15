# ejercicio 10
# Realizar un programa para ingresar desde el teclado un conjunto de números. Al
# finalizar mostrar por pantalla el primer y último elemento ingresado. Finalizar la
# lectura con el valor -1.
contar = 0
primero = 0
ultimo = 0

num = int(input("Ingrese un número: "))

while(num != -1):
    contar +=1
    if(contar == 1):
        primero = num

    ultimo = num
    num = int(input("Ingrese otro número: "))

print("Se ingresaron %d números. El #1 fue el %d y el último el %d." %(contar,primero,ultimo))

