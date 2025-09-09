nro = int(input("Ingrese un numero: "))
contador = 0

if nro == 0:
    contador = 1
    

while nro != 0:
    nro = nro // 10
    contador += 1

print(f"La cantidad de digitos: {contador}")

