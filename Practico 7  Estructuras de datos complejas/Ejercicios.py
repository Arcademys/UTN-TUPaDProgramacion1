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

