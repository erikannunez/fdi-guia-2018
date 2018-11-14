#ejercicio 4
numA = int(input("Ingrese un número A: "))
numB = int(input("Ingrese un número B: "))

if (numA%numB == 0) and (numB%numA == 0):
    print("El número %d es múltiplo de %d, y el número %d es múltiplo de %d" %(numA,numB,numB,numA))
elif (numA%numB == 0) and (numB%numA != 0):
    print("El número %d es múltiplo de %d pero el número %d no es múltiplo de %d" % (numA, numB, numB, numA))
elif (numA%numB != 0) and (numB%numA == 0):
    print("El número %d no es múltiplo de %d pero el número %d es múltiplo de %d" % (numA, numB, numB, numA))
else:
    print("El número %d no es múltiplo de %d, y el número %d no es múltiplo de %d" % (numA, numB, numB, numA))