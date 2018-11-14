# ejercicio 5
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# si todos los años tienen 365 dias ...
def edad_a_dias(edad):
    return edad * 365

# usando la funcion fecha
# def edad_a_dias_pro(edad):
#    return (datetime.now() - relativedelta(years=edad)).days

print(edad_a_dias(31))

# print(edad_a_dias_pro(31))