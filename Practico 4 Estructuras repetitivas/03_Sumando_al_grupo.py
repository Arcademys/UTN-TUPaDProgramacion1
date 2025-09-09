nro1 = int(input("Ingresa un numero: "))
nro2 = int(input("ingresa otro numero: "))
menor, mayor = sorted([nro1,nro2])
suma = 0



for i in range (menor +1, mayor ):
        suma +=  i
print(f"Suma entre {menor} y {mayor} es: {suma}")