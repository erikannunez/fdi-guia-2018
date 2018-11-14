# ejercicio 6
costoBasico = 125
costoLibro = 0

#encuadernacion rustica
costoPagina = 2.20
# encuadernacion en tela
encuadernacionTela = 80
# encuadernacion especial
encuadernacionEspecial = encuadernacionTela + 136

cantPags = int(input("Ingrese la cantida de paginas del libro: "))
if cantPags > 0:
    if cantPags <= 300:
        costoLibro = costoBasico + (costoPagina*cantPags)
    elif cantPags > 300 and cantPags <= 600:
        costoLibro = (costoBasico+encuadernacionTela) + (costoPagina*cantPags)
    else:
        costoLibro = (costoBasico+encuadernacionEspecial) + (costoPagina*cantPags)
    print("El costo total del libro es de $%.2f" %costoLibro)
else:
    print("El libro debe tener al menos una página :|")