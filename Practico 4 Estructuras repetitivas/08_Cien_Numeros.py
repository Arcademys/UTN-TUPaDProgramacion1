pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    nro = int(input("Ingrese un numero: "))
    if nro % 2 ==0:
        pares += 1
    else:
        impares += 1
    if nro > 0:
        positivos += 1
    elif nro < 0:
        negativos += 1

print(f"Numeros pares:{pares}, impares: {impares}, numeros positivos: {positivos} y numeros negativos: {negativos}")