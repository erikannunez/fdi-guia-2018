#ejercicio 5
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

if base < 0 or altura < 0:
    print("Los numeros ingresados deben ser positivos.")
else:
    superficie = (base*altura)/2
    print("La superficie del triángulo es de %.2f" %superficie)
