import random

secreto = random.randint(0,9)
intento = 0
numero = -1

while secreto != numero:
    numero = int(input("Ingrese un numero entre 0 y 9: "))
    intento += 1
    if numero == secreto:
     print(f"¡Felicidades! Descubriste el número secreto {secreto} en {intento} intentos.")
     