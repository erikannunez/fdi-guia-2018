# ejercicio 11
anio = int(input("Ingrese un año: "))

a = anio%19
b = anio%4
c = anio%7
d = ((a*19) + 24)%30
e = ((b*2 + c*4 + d*6) + 5)%7
fechaPascua = d + e + 22

if(fechaPascua > 31):
    print("La fecha de Pascua será el %d de abril!" %(fechaPascua-31))
else:
    print("La fecha de Pascua será el %d de marzo!" %fechaPascua)