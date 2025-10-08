tempetaruras = []

for dia in range(1, 8):
    print (f"Dia {dia}:")
    temp_min = float(input("Ingrese la temperatura minima: "))
    tem_max = float(input("Ingrese la temperatura maxima: "))
    sublista_temperaturas = [temp_min, tem_max]
    tempetaruras.append(sublista_temperaturas)

suma_max = 0
suma_min = 0
for dia in tempetaruras:
    suma_min = suma_min + temp_min
    promedio_min = suma_min / 7

suma_max = 0
for dia in tempetaruras:
    suma_max = suma_max + temp_min
    promedio_min = suma_max / 7

amplitud_mayor = 0
dia_mayor_amplitud = 0
for i in range(7):
    amplitud = tempetaruras [i] [1] - tempetaruras [i] [0]
    if amplitud > amplitud_mayor:
        amplitud_mayor = amplitud
        dia_mayor_amplitud = i + 1 

print(f"Promedio de temperaturas minimas: {promedio_min}, promedio de temperaturas maximas: {suma_max}")
