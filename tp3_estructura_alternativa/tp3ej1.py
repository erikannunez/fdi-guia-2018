# ejercicio 1
num1 = float(input("Ingrese un numero A: "))
num2 = float(input("Ingrese un numero B: "))

if num1 > num2:
    print("El mayor es: %f" %num1)
elif num2 > num1:
    print("El mayor es: %f" %num2)
else:
    print("Ambos números son iguales: %f" %num1)