
Lista_Notas = [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
print ("LISTAS DE NOTAS")

for i in (Lista_Notas):
    print(i)

#Calcular el promedio
promedio = sum(Lista_Notas) / len(Lista_Notas)

print (F"El promedio de las notas es: {promedio}")

#Calcular la nota mas alta
Nota_Mayor = max(Lista_Notas)
Nota_Menor = min(Lista_Notas)

print (f"La nota mayor es: {Nota_Mayor}")
print (f"La nota menor es: {Nota_Menor}")

