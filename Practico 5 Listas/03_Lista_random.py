import random

lista_numeros = []
for _ in range(15):
    nro_aleatorio = random.randint(1,100)
    lista_numeros.append(nro_aleatorio)

print("Lista completa de numeros:")
for nro in lista_numeros:
    print(nro)

nros_pares = []
nros_impares = []

for nro in lista_numeros:
    if nro % 2 == 0:
        nros_pares.append(nro)
    else:
        nros_impares.append(nro)

print("Lista de numeros pares:")
for nro in nros_pares:
    print(nro)

print("Lista de numeros impares:")
for nro in nros_impares:
    print(nro)

print(f"Cantidad de numeros pares:{len(nros_pares)}")
print(f"Cantidad de numeros impares:{len(nros_impares)}")