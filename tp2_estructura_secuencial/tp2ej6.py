# ejercicio 6
metros = float(input("Ingrese cantidad de metros: "))

centimetros = metros * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print("Centímetros: %.2f cm" %centimetros)
print("Pulgadas: %.2f" %pulgadas)
print("Pies: %.2f" %pies)
print("Yardas: %.2f" %yardas)
