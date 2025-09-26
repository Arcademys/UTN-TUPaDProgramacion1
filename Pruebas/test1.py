print("Contador Binario de 0 a 15:\n")

for i in range(16):
    n = i
    restos = []             # acá vamos a guardar los bits

    if n == 0:
        binario = "0"
    else:
        while n > 0:
            restos.append(str(n % 2))  # guardamos el resto
            n //= 2                    # dividimos por 2

        restos.reverse()               # invertimos para formar el número
        binario = "".join(restos)

    print(f"Decimal: {i} -> Binario: {binario}")