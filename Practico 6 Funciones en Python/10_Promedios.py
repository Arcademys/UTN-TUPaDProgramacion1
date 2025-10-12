def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))


resultado = calcular_promedio(num1, num2, num3)


print(f"El promedio de los tres numeros es: {resultado:.2f}")

