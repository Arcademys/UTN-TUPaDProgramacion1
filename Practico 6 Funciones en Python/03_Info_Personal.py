def informacion_personal(nombre, apellido,edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))