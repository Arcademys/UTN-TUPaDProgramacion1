lista_numeros = [10, 20, 30, 40, 50, 60, 70]
ultimo = lista_numeros[-1]

for i in range(len(lista_numeros) - 1, 0, -1):
    lista_numeros[i] = lista_numeros[i - 1]

lista_numeros[0] = ultimo
for i in lista_numeros:
    print(i)
