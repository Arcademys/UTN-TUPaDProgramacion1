nro = int(input("Ingrese un numero: "))
invertido = 0

while nro != 0:
    udigito = nro % 10
    invertido = invertido * 10 + udigito
    nro = nro // 10

print(f"El numero se invertio: {invertido}")