import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingrese el valor del radio: "))

print(f"El perimetro es de: {calcular_perimetro_circulo(radio)}, y el area es de: {calcular_area_circulo(radio)}")
