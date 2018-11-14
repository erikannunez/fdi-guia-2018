# ejercicio 4
import math
def superficieCirculo(r):
    return math.pi * (r**2)

def perimetroCircunferencia(d):
    return math.pi * d

def superficieEsfera(r):
    return 4 * math.pi * (r**2)

def volumenEsfera(r):
    return (4/3) * math.pi * (r**3)

# ingresar la longitud del radio de un circulo
radio = 4
diametro = radio * 2

print("--- Radio: %d"%radio)
print("--- Diámetro: %d"%diametro)
print("Superficie: %f" %superficieCirculo(radio))
print("Perimetro Circunferencia: %f" %perimetroCircunferencia(diametro))
print("Superficie Esfera: %f" %superficieEsfera(radio))
print("Volumen Esfera: %f" %volumenEsfera(radio))
