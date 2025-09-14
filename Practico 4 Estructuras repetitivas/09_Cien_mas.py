suma = 0

cantidad = int(input("Ingresa la cantidad de numeros a prosesar: "))

for i in range(cantidad):
    nro = int(input("Ingrese un numero: "))
    suma = suma + nro

media = suma / cantidad
print(f"La media es: {media}")