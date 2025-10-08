
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_nueva = []
for i in datos:
    if i not in lista_nueva:
        lista_nueva.append(i)

print("Lista sin elementos repetidos:")

for i in lista_nueva:
    print(i)