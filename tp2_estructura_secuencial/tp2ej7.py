# ejercicio 7
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio = (num1+num2+num3)/3

print("Promedio: %.2f" %promedio)


## otra forma:
ingresar = True
cantidad = 0
suma = 0
while(ingresar):
    num = int(input("Ingrese un numero: "))
    suma += num
    cantidad += 1
    ingresar = True if (input("Ingresar otro? [s/n]: ") == "s") else False

prom = suma/cantidad
print("Promedio: %.2f" %prom)