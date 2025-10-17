print("Ejercicio1\n")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200 
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


print("Ejercicio 2\n")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

print("Ejercicio 3\n")

lista_frutas = ["Banana", "Anana", "Melon", "Uva", "Naranja", "Manzana", "Pera"]

print(lista_frutas)

print("Ejercicio 4\n")

contactos = {}

for i in range(5):
    nombre = input("Ingrese nombre de contacto: ")
    nro_tel = input("Ingrese numero telefonico: ")
    contactos[nombre] = nro_tel

consulta = input("Ingrese contacto: ")

if consulta in contactos:
    print(contactos[consulta])
else:
    print("Contacto no encontrado")

print("Ejercicio 5\n")

frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] +=1
    else:
        recuento[palabra] = 1

print("Palabras", palabras_unicas)
print("Recuento:", recuento)


print("Ejercicio 6\n")


alumnos = {}


for i in range(3):
    

    
    nota1 = float(input("Ingrese nota 1: "))
    nota2 = float(input("Ingrese nota 2: "))
    nota3 = float(input("Ingrese nota 3: "))


    notas = (nota1, nota2, nota3)

  
    alumnos[nombre] = notas


print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(nombre, "→ Promedio:", promedio)


print("Ejercicio 7\n")

parcial1 = {"A", "B", "C", "D"}
parcial2 = {"C", "D", "E", "F"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos: ", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial: ", al_menos_uno)




