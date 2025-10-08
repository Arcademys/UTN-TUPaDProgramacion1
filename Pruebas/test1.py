print("Contador Binario de 0 a 15:\n")

lista_binarios = []

for i in range(16):                         #Bucle
    n = i
    restos = []

    if n == 0:                              #Condicional
        binario = "0"
    else:
        while n > 0:                        #Bucle
            restos.append(str(n % 2))       #Modulo resto
            n //= 2

        restos.reverse()
        binario = "".join(restos)

    lista_binarios.append(binario) # binarios guardados
    print(f"{i:2} -> {binario}")


print("\nLista completa de binarios:")
print(lista_binarios)




