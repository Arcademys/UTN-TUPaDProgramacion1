nro1 = int(input("Ingrese un numero:"))
nro2 = int(input("Ingrese otro numero:"))

resu1 = nro1 + nro2
resu2 = nro1 - nro2
resu3 = nro1 * nro2
resu4 = float(nro1/nro2)

if nro1 == 0 or nro2 == 0:
    print("Error")
else:
    print(f"El resultado de la suma es de:{resu1}, de la resta:{resu2}, de la multiplicaciones de:{resu3}, de la division: {resu4}.")

    