# ejercicio 13
sueldoBasico = float(input("Ingrese el sueldo básico: $"))
antiguedad = int(input("Ingrese antigüedad: "))
estadoCivil = input("Ingrese estado civil [s/c]:")
sueldoNeto, sueldoBruto, incremento, dctoJubilacion, dctoObraSocial, dctoSindicato = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

if(sueldoBasico > 0 and antiguedad >= 0 and (estadoCivil == "s" or estadoCivil == "c")):

    # asignamos el incremento por antiguedad que corresponde
    if(estadoCivil == "s"):
        incremento = 0.05
    else:
        incremento = 0.07

    # calculamos el sueldo bruto en base a la antiguedad y el incremento
    if(antiguedad > 0):
        sueldoBruto = sueldoBasico + (antiguedad * (sueldoBasico*incremento))
    else:
        sueldoBruto = sueldoBasico

    # calculamos los descuentos
    dctoJubilacion = sueldoBruto * 0.11
    dctoObraSocial = sueldoBruto * 0.03
    dctoSindicato = sueldoBruto * 0.03

    sueldoNeto = sueldoBruto - dctoJubilacion - dctoObraSocial - dctoSindicato

    # imprimimos el recibo
    print("Estado Civil: %s" %("Soltero" if estadoCivil == "s" else "Casado"))
    print("Sueldo básico \tAntigüedad \tDescuentos \tImporte")
    print("$%.2f \t\t%d años\t\t\t\t\t+%.2f" %(sueldoBasico,antiguedad,sueldoBruto))
    print("\t\t\t\tJubilación\t\t\t\t-%.2f" %dctoJubilacion)
    print("\t\t\t\tObra Social\t\t\t\t-%.2f" %dctoObraSocial)
    print("\t\t\t\tSindicato\t\t\t\t-%.2f" %dctoSindicato)
    print("\t\t\t\t\t\t\t\t\t\t------------")
    print("\t\t\t\tSueldo Neto\t\t\t\t%.2f" %sueldoNeto)

else:
    print("Los datos ingresados no son correctos. No se puede calcular.")