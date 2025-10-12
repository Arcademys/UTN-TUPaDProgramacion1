def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

resultado = operaciones_basicas(10 , 2)

print("Resultados de las operaciones basicas:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicacion: {resultado[2]}")
print(f"Division: {resultado[3]}")

