# ejercicio 2

ingresar = True
contar = 0
suma = 0

# ponemos la condicion "ingresar" para no obligar al usuario a cargar 100 nros.
while(ingresar and contar <=100):
    num = int(input("Ingrese un número: "))
    if(num != 0):
        contar += 1
        suma += num
        ingresar = True if input("Ingresar otro? [s/n]: ") == "s" else False
    else:
        num = input("El cero no se promedia! Ingrese otro: ")

print("Se ingresaron %d números que suman un total de %.2f. Su promedio es: %.2f" %(contar,suma,suma/contar))