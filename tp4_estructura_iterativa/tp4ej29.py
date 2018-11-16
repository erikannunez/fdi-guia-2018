# ejercicio 29
# Juancito está descontento con su rendimiento en las clases de Programación. En
# su primer programa cometió un error, en el segundo dos, en el tercero cuatro,
# en el cuarto ocho y así sucesivamente. Las clases duran S semanas y debe reali-
# zar dos programas semanales. Diseñar un programa que lea S y calcule el núme-
# ro de errores que Juancito debe esperar cometer en su último programa, si man-
# tiene constante su rendimiento actual. Resolver este problema utilizando dos
# estrategias distintas.

semanas = int(input("Ingrese la cantidad de semanas: "))
rendimiento = 1
programas = 0
for semana in range(semanas):
    for p in range(2):
        programas +=1
        print("Programa #%d (Semana #%d): %d errores!" %(programas,semana+1,rendimiento))
        rendimiento *= 2
