# ejercicio 16
# Dadas las siguientes series numéricas, desarrollar programas que muestren los primeros 20 términos de cada una de ellas.
# a. 1, 1, 2, 3, 4, 9, 8, 27, 16...
# es decir 2^0, 3^0, 2^1, 3^1, 2^2, 3^2, 2^3, 3^3...
#
# b. -1, 2, -3, 4, -5, 6, -7...
# es decir 1*(-1)^1, 2*(-1)^2, 3*(-1)^3, 4*(-1)^4, 5*(-1)^5, 6*(-1)^6, 7*(-1)^7...
#
# c. 1, 2, 4, 7, 11, 16, 22, 29...
# es decir 1, (1+1), (2+2), (4+3), (7+4), (11+5), (16+6), (22+7)...
# (el primer término es 1 y cada nuevo término se obtiene sumando el término anterior más el número de orden del término actual)

# A
base = 2
exponente = 0
for i in range(20):
    if base == 2:
        print(base**exponente)
        base +=1
    else:
        print(base**exponente)
        base -= 1
        exponente +=1

# B
for i in range(20):
    print((i+1)*(-1)**(i+1))

# C
anterior = 1
for i in range(20):
    print(anterior + i)
    anterior += i