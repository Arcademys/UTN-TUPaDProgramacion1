hem = int(input("Ingrese 1- Hemisferio norte 2- Hemisferio sur: "))
mes = int(input("Ingrese 1-Enero 2-Febrero 3-Marzo 4-Abril 5-Mayo 6-Junio 7-Julio 8-Agosto 9-Septiembre 10-Octubre 11-Noviembre 12-Diciembre: "))
dia = int(input("Ingrese Fecha 1 - 31: " ))

if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
    
    if hem == 1:
        print("Invierno")
    else:
        print("Verano")
elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
    
    if hem == 1:
        print("Primavera")
    else:
        print("Otonio")
elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <=20):
    
    if hem == 1:
        print("Verano")
    else:
        print("Invierno")
elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
    
    if hem == 1:
        print("Otonio")
    else:
        print("Primavera")
