scale = float(input("Ingrese los datos Richter: "))
if scale < 3:
    print("Muy leve")
elif scale >= 3 and scale < 4:
    print("Leve")
elif scale >= 4 and scale < 5:
    print("Moderado")
elif scale >= 5 and scale < 6:
    print("Fuerte")
elif scale >= 6 and scale < 7:
    print("Muy Fuerte")
else:
    print("Extremo")2