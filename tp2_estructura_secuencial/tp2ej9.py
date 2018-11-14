# ejercicio 9
salario = 800
comisionPorVenta = 50
porcentajeComision = 0.05

vendedor = int(input("Ingrese nro de vendedor: "))
cantVtas = int(input("Ingrese la cantidad de ventas realizadas: "))
totalVtas = float(input("Ingrese el importe total de las ventas realizadas: "))

salarioTotal = salario + (comisionPorVenta*cantVtas) + (totalVtas*porcentajeComision)

print("El salario a abonar al vendedor #%d es de $%.2f" %(vendedor,salarioTotal))