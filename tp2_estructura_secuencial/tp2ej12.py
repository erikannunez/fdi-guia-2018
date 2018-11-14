# ejercicio 12
binario = int(input("Ingrese un numero binario de 4 cifras -solo unos y ceros-: "))
original = binario
decimal = 0

# Ejemplo: se ingresa 1010
# separamos la ultima cifra: 101[0] para quedarnos solo con el 0 --> tmp = 0
tmp = binario%10
# sumamos al valor decimal la cifra separada elevada a cero: decimal += 0 * (2**0)
decimal += tmp*(2**0)
# actualizamos el nro para quedarnos con las otras tres cifras: binario = 101
binario = int(binario/10)
# nuevamente nos quedamos con el resto del binario de 3 cifras: 10[1] --> tmp = 1
tmp = binario%10
# sumamos al decimal la nueva cifra separada, elevada a uno: decimal += 1 * (2**1)
decimal += tmp * (2**1)
# actualizamos el nro para quedarnos con las otras dos cifras: binario = 10
binario = int(binario/10)
# separamos la tercer cifra: 1[0] --> tmp = 0
tmp = binario%10
# sumamos la cifra al decimal: decimal += 0 * (2**2)
decimal += tmp * (2**2)
# actualizamos el binario para quedarnos con la ultima cifra: binario = 1
binario = int(binario/10)
# separamos la ultima cifra: [1] --> tmp = 1
tmp = binario%10
# sumamos al decimal la ultima cifra
decimal += tmp * (2**3)
# actualizamos el binario
binario = int(binario/10)
print("El nro. binario %d equivale al decimal %d" %(original,decimal))
