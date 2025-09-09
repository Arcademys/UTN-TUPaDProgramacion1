nro1 = int(input("Ingresa un numero: "))
nro2 = int(input("ingresa otro numero: "))
suma = 0

if nro1 < nro2:
    
    for i in range (nro1, nro2 -1):
        suma +=  i
    
    print(f"{suma}")