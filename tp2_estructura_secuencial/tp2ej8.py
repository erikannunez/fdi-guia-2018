# ejercicio 8
periodo = int(input("Ingrese periodo en cantidad de segundos: "))

dias = (periodo / 86400)
horas = ((periodo % 86400) / 3600)
minutos = (((periodo % 86400) % 3600) / 60)
segundos = ((periodo % 86400) % 3600) % 60

print("%d segundos equivales a %d dias %d horas %d minutos y %d segundos" %(periodo,dias,horas,minutos,segundos))